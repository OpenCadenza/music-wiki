#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Probe **kern: spine ops, token syntax, measure numbers.

Usage: python kern_probe.py <file.krn> [m0] [m1]
"""
import re
import sys
from collections import Counter

NOTE_RE = re.compile(r'^(?P<pre>[^0-9]*)(?P<dur>\d+\.*)(?P<letters>[A-Ga-g]+)'
                     r'(?P<acc>[#nXx-]*)(?P<suf>.*)$')
REST_RE = re.compile(r'^(?P<pre>[^0-9]*)(?P<dur>\d+\.*)r(?P<suf>.*)$')


def process_ops(toks, spines, next_voice):
    """Return new spine list given interpretation tokens."""
    out = []
    i = 0
    while i < len(toks):
        t = toks[i]
        cur = spines[i]
        if t == '*^':
            out.append(dict(cur, voice=next_voice[0]))
            next_voice[0] += 1
            out.append(dict(cur, voice=next_voice[0]))
            next_voice[0] += 1
            i += 1
        elif t == '*v':
            # merge current with next spine; skip next token
            nxt = spines[i + 1] if i + 1 < len(spines) else cur
            out.append(dict(cur, voice=cur.get('voice', 0)))
            i += 2
        else:
            new = dict(cur)
            m = re.match(r'\*staff(\d+)', t)
            if m:
                new['staff'] = int(m.group(1))
            m = re.match(r'\*clef(\S+)', t)
            if m:
                new['clef'] = m.group(1)
            m = re.match(r'\*k\[(.*?)\]', t)
            if m:
                new['key'] = m.group(1)
            out.append(new)
            i += 1
    return out


def main():
    path = sys.argv[1]
    m0 = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    m1 = int(sys.argv[3]) if len(sys.argv) > 3 else 10 ** 9
    lines = open(path, encoding='utf-8', errors='replace').read().splitlines()
    header = None
    for ln in lines:
        if ln.startswith('**'):
            header = ln.split('\t')
            break
    print('FILE', path)
    print('SPINES', header)
    spines = [dict(voice=i, staff=None, clef=None, type=h.lstrip('*')) for i, h in enumerate(header)]
    next_voice = [len(header)]
    cur = None
    keys = {}
    meters = {}
    tempos = {}
    prefixes = Counter()
    suffixes = Counter()
    restsuf = Counter()
    unparsed = Counter()
    staff_hist = Counter()
    for ln in lines:
        if not ln.strip():
            continue
        if ln.startswith('**'):
            continue
        if ln.startswith('*'):
            toks = ln.split('\t')
            if len(toks) != len(spines):
                print('!! interp count', len(spines), len(toks), repr(ln))
                continue
            for i, t in enumerate(toks):
                m = re.match(r'\*M(\S+)', t)
                if m:
                    meters[cur] = m.group(1)
                m = re.match(r'\*MM(\d+)', t)
                if m:
                    tempos[cur] = int(m.group(1))
                if t.startswith('*k['):
                    keys[cur] = t[3:-1]
            spines = process_ops(toks, spines, next_voice)
            continue
        if ln.startswith('='):
            mm = re.match(r'=(\d+)', ln)
            if mm:
                cur = int(mm.group(1))
            continue
        if ln.startswith('!'):
            continue
        toks = ln.split('\t')
        if len(toks) != len(spines):
            print('!! data count', len(spines), len(toks), 'm', cur, repr(ln))
            continue
        staff_hist[tuple(s['staff'] for s in spines)] += 1
        if not (m0 <= (cur or 0) <= m1):
            continue
        for i, t in enumerate(toks):
            if spines[i]['type'] != 'kern':
                continue
            t = t.strip()
            if not t or t == '.':
                continue
            for piece in t.split():
                mr = REST_RE.match(piece)
                if mr:
                    restsuf[piece] += 1
                    continue
                mn = NOTE_RE.match(piece)
                if mn:
                    prefixes[mn.group('pre')] += 1
                    suffixes[mn.group('suf')] += 1
                else:
                    unparsed[piece] += 1
    print('staff layouts', staff_hist.most_common(8))
    print('keys', keys)
    print('meters', meters)
    print('tempos', tempos)
    print('prefixes', prefixes.most_common(30))
    print('suffixes', suffixes.most_common(40))
    print('rest tokens', restsuf.most_common(20))
    print('unparsed', unparsed.most_common(20))


if __name__ == '__main__':
    main()
