"""Exact diff: DCML mm1-8 note positions (pitch,onset) vs compiled MIDI from the .ly."""
import xml.etree.ElementTree as ET
import struct

DCML = r"E:\github\music-wiki\.agents\worktrees\scholar-plan-dev\local\resources\scores\score-s6\beethoven-op109\dcml-30-3.musicxml"
import sys
MIDI = sys.argv[1] if len(sys.argv) > 1 else r"lp-build.mid"
STEP = {"C":0,"D":2,"E":4,"F":5,"G":7,"A":9,"B":11}

# ---------- DCML ----------
def dcml_notes():
    out = {}   # (measure:int) -> list of (pitch, onset_q, dur_q)
    root = ET.parse(DCML).getroot()
    for part in root.findall("part"):
        for meas in part.findall("measure"):
            try: mn = int(meas.get("number"))
            except (TypeError, ValueError): continue
            if not (1 <= mn <= 8): continue
            div = 240
            for a in meas.findall("attributes"):
                if a.findtext("divisions"): div = int(a.findtext("divisions"))
            cur = 0; prev = 0
            for el in meas:
                if el.tag == "backup":
                    cur -= int(el.findtext("duration") or 0)
                elif el.tag == "forward":
                    cur += int(el.findtext("duration") or 0)
                elif el.tag == "note":
                    if el.find("grace") is not None: continue
                    d = int(el.findtext("duration") or 0)
                    if el.find("chord") is None:
                        if el.find("rest") is not None:
                            cur += d; prev = d; continue
                        on = cur; cur += d; prev = d
                    else:
                        on = cur - prev
                    p = el.find("pitch")
                    m = 12*(int(p.findtext("octave"))+1)+STEP[p.findtext("step")] + (int(p.findtext("alter")) if p.findtext("alter") not in (None,"") else 0)
                    out.setdefault(mn, []).append((m, on/div, d/div, part.get("id")))
    return out

# ---------- MIDI ----------
def rd(d,i):
    v=0
    while True:
        b=d[i]; i+=1; v=(v<<7)|(b&0x7f)
        if not b&0x80: return v,i

def midi_notes():
    data=open(MIDI,"rb").read()
    hl=struct.unpack(">I",data[4:8])[0]
    fmt,ntr,div=struct.unpack(">HHH",data[8:14])
    pos=8+hl; notes=[]
    for _ in range(ntr):
        tl=struct.unpack(">I",data[pos+4:pos+8])[0]
        body=data[pos+8:pos+8+tl]; pos+=8+tl
        i=0; tick=0; run=None; pend={}
        while i<len(body):
            dt,i=rd(body,i); tick+=dt
            b=body[i]
            if b==0xff:
                i+=1; meta=body[i]; i+=1
                ln,i=rd(body,i); i+=ln
                if meta==0x2f: break
                continue
            if b in (0xf0,0xf7):
                i+=1; ln,i=rd(body,i); i+=ln; continue
            if b&0x80: st=b; i+=1; run=st
            else: st=run
            hi=st&0xf0
            if hi in (0x80,0x90):
                p=body[i]; v=body[i+1]; i+=2
                if hi==0x90 and v>0: pend.setdefault(p,[]).append(tick)
                elif pend.get(p): notes.append((pend[p].pop(0), tick-pend[p][0] if False else 0,0))
                continue
            if hi in (0xa0,0xb0,0xe0): i+=2; continue
            if hi in (0xc0,0xd0): i+=1; continue
    # simpler & correct 2nd pass
    notes=[]
    pos=8+hl
    for _ in range(ntr):
        tl=struct.unpack(">I",data[pos+4:pos+8])[0]
        body=data[pos+8:pos+8+tl]; pos+=8+tl
        i=0; tick=0; run=None; pend={}
        while i<len(body):
            dt,i=rd(body,i); tick+=dt
            b=body[i]
            if b==0xff:
                i+=1; meta=body[i]; i+=1; ln,i=rd(body,i); i+=ln
                if meta==0x2f: break
                continue
            if b in (0xf0,0xf7):
                i+=1; ln,i=rd(body,i); i+=ln; continue
            if b&0x80: st=b; i+=1; run=st
            else: st=run
            hi=st&0xf0
            if hi in (0x80,0x90):
                p=body[i]; v=body[i+1]; i+=2
                if hi==0x90 and v>0: pend.setdefault(p,[]).append(tick)
                elif pend.get(p):
                    on=pend[p].pop(0); notes.append((on,tick-on,p))
                continue
            if hi in (0xa0,0xb0,0xe0): i+=2; continue
            if hi in (0xc0,0xd0): i+=1; continue
    out={}
    for on,dur,p in notes:
        if dur/div < 0.2:   # grace notes (LilyPond renders them very short)
            continue
        mn = int(on/(3*div))+1
        out.setdefault(mn,[]).append((p,(on-(mn-1)*3*div)/div,dur/div))
    return out

dn=dcml_notes(); mn_=midi_notes()
allok=True
for m in range(1,9):
    a=sorted((round(o*4),p) for p,o,d,_ in dn.get(m,[]))
    b=sorted((round(o*4),p) for p,o,d in mn_.get(m,[]))
    print(f"measure {m}: DCML {len(a)} notes, MIDI {len(b)} notes -> ", end="")
    if a==b:
        print("POSITIONS MATCH")
    else:
        allok=False
        print("DIFF")
        from collections import Counter
        ca,cb=Counter(a),Counter(b)
        print("   only in DCML:", sorted((ca-cb).elements()))
        print("   only in MIDI:", sorted((cb-ca).elements()))
    # duration check on unambiguous (1-to-1) matches
    da={}
    for p,o,d,pid in dn.get(m,[]): da.setdefault((round(o*4),p),[]).append(round(d,3))
    db={}
    for p,o,d in mn_.get(m,[]): db.setdefault((round(o*4),p),[]).append(round(d,3))
    for k in sorted(set(da)&set(db)):
        if da[k]!=db[k]:
            # tolerate grace-stealing (0.85..1.0) and unison-merge (two events -> one long)
            tag="ok(tolerated)"
            if len(db[k])<len(da[k]): tag="OK unison-merged in MIDI"
            elif all(abs(x-y)<0.2 for x,y in zip(da[k],db[k])): tag="OK grace-steal"
            else: tag="DURATION MISMATCH"; allok=False
            print(f"   dur @{k}: DCML={da[k]} MIDI={db[k]}  {tag}")

# range
lo=min(p for m in mn_ for p,_,_ in mn_[m])
hi=max(p for m in mn_ for p,_,_ in mn_[m])
print(f"\nMIDI pitch range: {lo}..{hi}  (A0={21}, C8={108}) -> within piano: {lo>=21 and hi<=108}")
print("\nOVERALL NOTE-LEVEL:", "MATCH" if allok else "DIFFERENCES FOUND")