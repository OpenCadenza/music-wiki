import pandas as pd
import subprocess

# Let's compile beethoven-op74-mvt1-mm1-9-adagio.ly and extract midi notes
res = subprocess.run([r'E:\GreenSoftware\lilypond-2.26.0\bin\lilypond.exe', '-o', 'local/workbench/scores/assistant-scores-a/temp_b_op74', 'local/resources/scores/beethoven-op74/beethoven-op74-mvt1-mm1-9-adagio.ly'], capture_output=True, text=True)
print("Lilypond compilation:", res.returncode)
if res.stderr:
    print("Stderr:", res.stderr[:500])

with open('local/workbench/scores/assistant-scores-a/temp_b_op74.mid', 'rb') as f:
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
ly_tracks = {}
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
        curr_time = 0
        while t_idx < len(track_data):
            delta, t_idx = parse_vlq(track_data, t_idx)
            curr_time += delta
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
                    notes.append((curr_time, pitch))
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
        print(f"Track {track_num} ({name}): count={len(notes)}")
        if notes:
            ly_tracks[name] = notes

# Read DCML notes
df = pd.read_csv('local/resources/scores/dcml-abc/n10op74_01.notes.tsv', sep='\t')
# Exclude tied continuation notes! In DCML notes.tsv, tied == -1 indicates a note continuation tied from previous note!
df_mm = df[df['mn'] <= 9].copy()
df_mm_starts = df_mm[df_mm['tied'] != -1]

print("\n--- DCML mm. 1-9 notes (non-tied-starts) count by staff ---")
for s in [1, 2, 3, 4]:
    sub = df_mm_starts[df_mm_starts['staff'] == s]
    print(f"Staff {s}: count={len(sub)}, notes={list(sub['name'])}, midi={list(sub['midi'])}")
