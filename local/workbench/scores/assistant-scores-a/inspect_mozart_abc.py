# Let's inspect the Mozart ABC file measures 0 to 10
with open('local/origin_resources/corpus/abc/humdrum-kern/mozart_sonatas/0013-13-Piano Sonata No. 5 in G major, K 283 (189h), mvmt. 1.abc', 'r') as f:
    lines = f.readlines()

print("Mozart ABC lines 24 to 50:")
for i in range(24, 50):
    print(f"{i+1}: {lines[i].strip()}")
