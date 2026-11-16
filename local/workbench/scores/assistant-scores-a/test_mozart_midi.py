import subprocess

# Compile mozart-k283-mvt1-mm1-10.ly and check MIDI notes
res = subprocess.run([r'E:\GreenSoftware\lilypond-2.26.0\bin\lilypond.exe', '-o', 'local/workbench/scores/assistant-scores-a/temp_mozart', 'local/resources/scores/mozart-k283/mozart-k283-mvt1-mm1-10.ly'], capture_output=True, text=True)
print("Lilypond compilation:", res.returncode)
if res.stderr:
    print("Stderr:", res.stderr[:500])

with open('local/workbench/scores/assistant-scores-a/temp_mozart.mid', 'rb') as f:
    data = f.read()

def parse_vlq(data, idx):
    val = 0
    while True:
        b = data[idx]
        idx += 1
        val = (val << 7) | (b & 0x7F)
        if not (b & 0x80):
            break
    return val, idx

idx = 14
track_num = 0
tracks_midi = []
while idx < len(data):
    if data[idx:idx+4] == b'MTrk':
        track_num += 1
        length = int.from_bytes(data[idx+4:idx+8], 'big')
        track_data = data[idx+8:idx+8+length]
        idx += 8 + length
        t_idx = 0
        running_status = None
        notes = []
        name = ''
        while t_idx < len(track_data):
            delta, t_idx = parse_vlq(track_data, t_idx)
            b = track_data[t_idx]
            if b >= 0x80:
                status = b
                t_idx += 1
                running_status = status
            else:
                status = running_status
            if (status & 0xF0) == 0x90:
                pitch = track_data[t_idx]
                vel = track_data[t_idx+1]
                t_idx += 2
                if vel > 0:
                    notes.append(pitch)
            elif (status & 0xF0) in (0x80, 0xA0, 0xB0, 0xE0):
                t_idx += 2
            elif (status & 0xF0) in (0xC0, 0xD0):
                t_idx += 1
            elif status == 0xFF:
                meta_type = track_data[t_idx]
                t_idx += 1
                meta_len, t_idx = parse_vlq(track_data, t_idx)
                if meta_type == 3:
                    name = track_data[t_idx:t_idx+meta_len].decode('latin1', errors='ignore')
                t_idx += meta_len
        print(f"Track {track_num} ({name}): notes={len(notes)}")
        if notes:
            tracks_midi.append((name, notes))

print("Track 1 notes:", tracks_midi[0][1])
print("Track 2 notes:", tracks_midi[1][1])
