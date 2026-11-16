"""最小 MIDI 音高提取 + 版本对比，用于谱例修正的独立核验。

用法：
  python local/workbench/tools/midi_pitch_check.py <文件A.mid> [文件B.mid]

输出：每个文件的音高范围（MIDI 号 + 音名）、音符总数、按时间排序的前若干个音高；
若给了第二个文件，额外输出两文件的逐音差（用于确认"只改了该改的八度"）。
"""

import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
INSTRUMENT_RANGES = {
    # MIDI 号区间（含端点）
    "piano": (21, 108),      # A0–C8
    "violin": (55, 103),     # G3–G7 常用上限，按演奏实际放宽到 C8
    "viola": (48, 88),       # C3–E6
    "cello": (36, 76),       # C2–E5
}


def read_vlq(data, index):
    value = 0
    while True:
        byte = data[index]
        index += 1
        value = (value << 7) | (byte & 0x7F)
        if not byte & 0x80:
            return value, index


def parse_midi(path):
    data = Path(path).read_bytes()
    if data[:4] != b"MThd":
        raise SystemExit(f"{path}: 不是标准 MIDI 文件")
    header_len = int.from_bytes(data[4:8], "big")
    index = 8 + header_len
    notes = []          # (start_tick, pitch, channel)
    divisions = int.from_bytes(data[12:14], "big")
    while index < len(data):
        if data[index:index + 4] != b"MTrk":
            break
        track_len = int.from_bytes(data[index + 4:index + 8], "big")
        cursor = index + 8
        end = cursor + track_len
        tick = 0
        running = None
        while cursor < end:
            delta, cursor = read_vlq(data, cursor)
            tick += delta
            if cursor >= end:
                break
            status = data[cursor]
            if status == 0xFF:            # meta 事件：0xFF、类型字节、VLQ 长度、数据
                cursor += 1
                cursor += 1               # 跳过 meta 类型字节
                length, cursor = read_vlq(data, cursor)
                cursor += length
                running = None            # meta 事件会清除 running status
                continue
            if status in (0xF0, 0xF7):    # sysex：0xF0/F7、VLQ 长度、数据
                cursor += 1
                length, cursor = read_vlq(data, cursor)
                cursor += length
                running = None
                continue
            if status & 0x80:
                cursor += 1
                running = status
            else:
                status = running
            if status is None:
                break
            kind = status & 0xF0
            channel = status & 0x0F
            if kind in (0x80, 0x90):
                pitch = data[cursor]
                velocity = data[cursor + 1]
                cursor += 2
                if kind == 0x90 and velocity > 0:
                    notes.append((tick, pitch, channel))
            elif kind in (0xA0, 0xB0, 0xE0):
                cursor += 2
            elif kind == 0xC0:
                cursor += 1
            elif kind == 0xD0:
                cursor += 1
            elif kind == 0xF0:
                length, cursor = read_vlq(data, cursor)
                cursor += length
            else:
                break
        index = end
    notes.sort()
    return notes, divisions


def name(pitch):
    return f"{NOTE_NAMES[pitch % 12]}{pitch // 12 - 1}"


def report(path):
    notes, divisions = parse_midi(path)
    pitches = [p for _, p, _ in notes]
    if not pitches:
        print(f"{path}: 没有音符事件")
        return pitches
    low, high = min(pitches), max(pitches)
    print(f"\n=== {path} ===")
    print(f"音符数 {len(pitches)}；音高范围 {name(low)}({low}) – {name(high)}({high})；divisions={divisions}")
    by_channel = {}
    for _, pitch, channel in notes:
        by_channel.setdefault(channel, []).append(pitch)
    for channel, values in sorted(by_channel.items()):
        print(
            f"  ch{channel + 1}: {len(values)} 音，范围 {name(min(values))}({min(values)})"
            f" – {name(max(values))}({max(values)})"
        )
    print("  前 12 个音（按时间）：" + " ".join(f"{name(p)}({p})" for p in pitches[:12]))
    legal = INSTRUMENT_RANGES["piano"]
    illegal = [p for p in pitches if not legal[0] <= p <= legal[1]]
    if illegal:
        print(f"  ⚠ 超出 88 键范围（A0–C8，MIDI 21–108）：{sorted(set(illegal))}")
    else:
        print("  ✓ 全部落在 88 键钢琴音域内")
    return pitches


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    first = report(sys.argv[1])
    if len(sys.argv) >= 3:
        second = report(sys.argv[2])
        count = min(len(first), len(second))
        deltas = [second[i] - first[i] for i in range(count)]
        print(f"\n=== 逐音差（第二个文件 − 第一个文件，前 {count} 音）===")
        print("  " + " ".join(f"{d:+d}" for d in deltas[:32]))
        unique = sorted(set(deltas))
        print(f"  出现的差值集合：{unique}")
        if unique == [0]:
            print("  → 两版音高完全相同")
        elif set(unique) <= {-12, 0, 12}:
            print("  → 差异全部是整八度位移，符合『八度基准修正』的预期形态")
        else:
            print("  → 存在非整八度的音高差异，需人工逐音核查")


if __name__ == "__main__":
    main()
