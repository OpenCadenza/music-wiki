"""贝多芬 Op.18 No.2 IV mm.1-8：被测件 vs DCML / OMT XML / kern-ABC。"""
import sys
sys.path.insert(0, ".")
import compare as C

BASE = "E:/github/music-wiki/.agents/worktrees/dsh-c6ded6ed-82bb/"
OMT_XML = BASE + "local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/Graphics/form/XML/beethoven_18_2.xml"
DCML = BASE + "local/resources/scores/dcml-abc/n02op18-2_04.notes.tsv"
ABC = BASE + "local/origin_resources/corpus/abc/humdrum-kern/beethoven_quartets/0008-8-String Quartet No. 2 in G Major, Op. 18, No. 2 mvt 4.abc"

names = ["violinOne", "violinTwo", "viola", "cello"]
ly = C.ly_per_measure("display_beethoven.txt", names, 2.0, 0.0)
dcml = C.dcml_per_measure(DCML, 8)
xml = C.xml_per_measure(OMT_XML, 8)
abc = C.abc_per_measure(ABC, 25, 56, unit=0.5, key_alters={"F": 1})
abc = {k + 1: v for k, v in abc.items()}   # ABC 字段下标 0 起 → 小节号 1 起
ms = list(range(1, 9))
C.show(ly, ms, "被测件 .ly")
C.show(dcml, ms, "DCML notes.tsv")
C.show(xml, ms, "OMT XML")
C.show(abc, ms, "kern-ABC")
print()
C.diff(ly, dcml, "被测件 vs DCML（音高）", ms)
C.diff(ly, dcml, "被测件 vs DCML（音高+时值）", ms, with_dur=True)
print()
C.diff(ly, xml, "被测件 vs OMT XML（音高）", ms)
C.diff(ly, xml, "被测件 vs OMT XML（音高+时值）", ms, with_dur=True)
print()
C.diff(ly, abc, "被测件 vs kern-ABC（音高）", ms)
C.diff(ly, abc, "被测件 vs kern-ABC（音高+时值）", ms, with_dur=True)
