import io
import sys

p = r'local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/Graphics/form/XML/beethovenop30.xml'
t = io.open(p, encoding='utf-8').read()
i = t.find('<score-part')
print('--- header ---')
print(t[i:i + 900])
j = t.find('<measure number="1"')
print('--- measure 1 ---')
print(t[j:j + 3500])
