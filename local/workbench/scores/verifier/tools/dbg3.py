import sys, os
sys.path.insert(0, os.getcwd())
import cmp_staff as C
for s in [r"b'2 <e' e''>2 |", r"\clef treble b'2 <e' e''>2 |", r"b'2 |"]:
    print(repr(s), '->', C.parse_block(s))
