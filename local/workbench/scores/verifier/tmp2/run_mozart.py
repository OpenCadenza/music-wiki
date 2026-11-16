"""莫扎特 K.330 II mm.1-8：被测件 vs OMT MusicXML vs kern-ABC。"""
import sys
sys.path.insert(0, ".")
import compare as C

BASE = "E:/github/music-wiki/.agents/worktrees/dsh-c6ded6ed-82bb/"
MOZ_XML = BASE + "local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/Graphics/form/XML/mozart, k330,ii.xml"
MOZ_ABC = BASE + "local/origin_resources/corpus/abc/humdrum-kern/mozart_sonatas/0041-41-Piano Sonata No. 10 in C major, K 330 (300h), mvmt. 2.abc"

ly = C.ly_per_measure("display_mozart.txt", ["rightHand", "leftHand"], 3.0, 1.5)
xml = C.xml_per_measure(MOZ_XML, 8)
abc = C.abc_per_measure(MOZ_ABC, 25, 42, unit=0.5, key_alters={"B": -1})
# ABC 行 42 是最后一行 V2 小节（bar 8），行 41 是 V1 bar 8
ms = list(range(0, 9))
C.show(ly, ms, "被测件 .ly（RH+LH 合并）")
C.show(xml, ms, "OMT MusicXML")
C.show(abc, ms, "kern-ABC")
print()
C.diff(ly, xml, "被测件 vs OMT XML", ms)
print()
C.diff(ly, abc, "被测件 vs kern-ABC", ms)
