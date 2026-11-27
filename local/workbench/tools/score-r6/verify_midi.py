#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""verify_midi (score-r6)：读 LilyPond 生成的 MIDI，抽出全部 note-on 音高，与底本音高多重集回比对。

用法：
  python verify_midi.py --mid a.mid --expect-file expected.json [--key voices.1]
expected.json: {"1": {"1": [..], "2": [..]}, ...}（abc2ly --dump/--json 同格式）
"""
import argparse
import json
import struct


def read_midi(path):
    data = open(path, "rb").read()
    if data[:4] != b"MThd":
        raise ValueError("不是 MIDI 文件")
    hlen = struct.unpack(">I", data[4:8])[0]
    fmt, ntrks, division = struct.unpack(">HHH", data[8:14])
    pos = 8 + hlen
    pitches = []
    for _ in range(ntrks):
        if data[pos:pos + 4] != b"MTrk":
            break
        tlen = struct.unpack(">I", data[pos + 4:pos + 8])[0]
        body = data[pos + 8:pos + 8 + tlen]
        pos += 8 + tlen
        i = 0
        status = None
        while i < len(body):
            # delta time
            while body[i] & 0x80:
                i += 1
            i += 1
            if i >= len(body):
                break
            b = body[i]
            if b & 0x80:
                status = b
                i += 1
            if status is None:
                break
            ev = status & 0xF0
            if ev in (0x80, 0x90, 0xA0, 0xB0, 0xE0):
                if ev == 0x90 and i + 1 < len(body):
                    pitch, vel = body[i], body[i + 1]
                    if vel > 0:
                        pitches.append(pitch)
                i += 2
            elif ev in (0xC0, 0xD0):
                i += 1
            elif status == 0xFF:
                meta = body[i]
                i += 1
                ln = body[i]
                i += 1 + ln
            elif status in (0xF0, 0xF7):
                ln = body[i]
                i += 1 + ln
            else:
                i += 1
    return pitches


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mid", required=True)
    ap.add_argument("--expect-file", required=True)
    ap.add_argument("--key", default="")
    args = ap.parse_args()
    got = sorted(read_midi(args.mid))
    exp = json.load(open(args.expect_file, encoding="utf-8"))
    if args.key:
        for part in args.key.split("."):
            exp = exp[part]
    want = sorted(v for vals in exp.values() for v in vals)
    miss = list(want)
    extra = list(got)
    for p in list(miss):
        if p in extra:
            miss.remove(p)
            extra.remove(p)
    print("MIDI 音高 %d 个，底本 %d 个；缺少 %d，多出 %d" % (len(got), len(want), len(miss), len(extra)))
    if miss:
        print("  缺少:", sorted(miss))
    if extra:
        print("  多出:", sorted(extra))
    return 0 if not miss and not extra else 1


if __name__ == "__main__":
    raise SystemExit(main())
