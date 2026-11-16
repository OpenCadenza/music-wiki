import pandas as pd

# Let's inspect MIDI pitches from LilyPond temp_b_op74.mid and compare with DCML
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
        if notes:
            tracks_midi.append((name, notes))

df = pd.read_csv('local/resources/scores/dcml-abc/n10op74_01.notes.tsv', sep='\t')
df_mm = df[df['mn'] <= 9].copy()
df_mm_starts = df_mm[df_mm['tied'] != -1]

names = ["Violin I", "Violin II", "Viola", "Cello"]
for i, s in enumerate([1, 2, 3, 4]):
    dcml_pitches = list(df_mm_starts[df_mm_starts['staff'] == s]['midi'])
    ly_pitches = tracks_midi[i][1]
    print(f"\n=== Staff {s}: {names[i]} ===")
    print("DCML: ", dcml_pitches)
    print("Lily: ", ly_pitches)
    if dcml_pitches == ly_pitches:
        print("RESULT: EXACT MATCH!")
    else:
        print("RESULT: DIFFERENCE!")
        for idx_p, (d, l) in enumerate(zip(dcml_pitches, ly_pitches)):
            if d != l:
                print(f"  Note {idx_p}: DCML={d} vs Lily={l}")
