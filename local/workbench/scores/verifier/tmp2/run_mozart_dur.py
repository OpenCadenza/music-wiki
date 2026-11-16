import sys
sys.path.insert(0, ".")
import compare as C
BASE = "E:/github/music-wiki/.agents/worktrees/dsh-c6ded6ed-82bb/"
MOZ_XML = BASE + "local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/Graphics/form/XML/mozart, k330,ii.xml"
ly = C.ly_per_measure("display_mozart.txt", ["rightHand", "leftHand"], 3.0, 1.5)
xml = C.xml_per_measure(MOZ_XML, 8)
C.diff(ly, xml, "被测件 vs OMT XML（含时值）", list(range(0, 9)), with_dur=True)
