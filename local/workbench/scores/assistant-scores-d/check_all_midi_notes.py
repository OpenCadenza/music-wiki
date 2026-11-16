with open('local/workbench/scores/assistant-scores-d/beethoven-op18-no2-mvt4-mm1-8.mid', 'rb') as f:
    data = f.read()

NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
def pname(p): return f"{NOTE_NAMES[p%12]}{p//12-1}({p})"

def parse_track(track_data):
    p = 0
    t = 0
    events = []
    running_status = None
    while p < len(track_data):
        dt = 0
        while True:
            b = track_data[p]
            p += 1
            dt = (dt << 7) | (b & 0x7F)
            if not (b & 0x80): break
        t += dt
        b = track_data[p]
        if b & 0x80:
            status = b
            p += 1
            running_status = status
        else:
            status = running_status
        if status == 0xFF:
            meta_type = track_data[p]; p += 1
            mlen = 0
            while True:
                mb = track_data[p]; p += 1
                mlen = (mlen << 7) | (mb & 0x7F)
                if not (mb & 0x80): break
            meta_val = track_data[p:p+mlen]
            p += mlen
            events.append((t, 'meta', meta_type, meta_val))
        elif (status & 0xF0) in (0x80, 0x90):
            p1 = track_data[p]; p += 1
            p2 = track_data[p]; p += 1
            events.append((t, 'note', status & 0xF0, status & 0x0F, p1, p2))
        elif (status & 0xF0) in (0xA0, 0xB0, 0xE0):
            p += 2
        elif (status & 0xF0) in (0xC0, 0xD0):
            p += 1
    return events

p = 14
track_no = 0
total_notes = 0
all_notes = []
while p < len(data):
    length = int.from_bytes(data[p+4:p+8], 'big')
    events = parse_track(data[p+8:p+8+length])
    name = 'Track ' + str(track_no)
    notes = []
    for e in events:
        if e[1] == 'meta' and e[2] == 3:
            name = e[3].decode('latin1', errors='replace')
        elif e[1] == 'note' and e[2] == 0x90 and e[5] > 0:
            notes.append((e[0], e[4], pname(e[4])))
            all_notes.append((e[0], track_no, name, e[4], pname(e[4])))
    print(f"=== {name} (Track {track_no}): {len(notes)} notes ===")
    for n in notes:
        print(f"  t={n[0]:4d} {n[2]}")
    total_notes += len(notes)
    p += 8 + length
    track_no += 1

print(f"\nTotal notes across all tracks: {total_notes}")
pitches = [n[3] for n in all_notes]
print(f"Pitch range: {pname(min(pitches))} – {pname(max(pitches))}")
