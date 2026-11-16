from PIL import Image
import numpy as np, sys
sys.stdout.reconfigure(encoding="utf-8")
src = r"local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/Graphics/form/k283.png"
a = np.array(Image.open(src).convert("L"))
dark = a < 128
TOP, SP = 355.5, 19.0   # 低音谱表最上线 A3, 线间距
def yname(y):
    step = (y - TOP) / (SP/2)   # 每半线 = 一个音级
    # 从 A3 起按音级递推（低音谱表最上线 = A3）
    seq_up = ["A3","B3","C4","D4","E4","F4","G4","A4","B4","C5"]
    seq_dn = ["A3","G3","F3","E3","D3","C3","B2","A2","G2","F2"]
    if step <= 0:
        i = min(int(round(-step)), len(seq_dn)-1)
        return seq_dn[i], -step
    i = min(int(round(step)), len(seq_up)-1)
    return seq_up[i], step

def blobs(x0,x1,y0,y1):
    pts=[]
    for x in range(x0,x1):
        col = dark[y0:y1, x]
        y=0
        while y < len(col):
            if col[y]:
                y2=y
                while y2+1 < len(col) and col[y2+1]: y2+=1
                L=y2-y+1
                if 6 <= L <= 16:
                    pts.append((x, (y+y2)/2.0+y0))
                y=y2+1
            else:
                y+=1
    return pts

def cluster(pts):
    pts=sorted(pts, key=lambda p:p[0])
    groups=[]
    for x,y in pts:
        placed=False
        for g in groups:
            if abs(g[-1][0]-x)<=3 and abs(g[-1][1]-y)<=4:
                g.append((x,y)); placed=True; break
        if not placed:
            groups.append([(x,y)])
    out=[]
    for g in groups:
        xs=[p[0] for p in g]; ys=[p[1] for p in g]
        if len(g)>=6:   # 有效符头
            out.append((sum(xs)/len(xs), sum(ys)/len(ys), len(g)))
    return out

for label, (x0,x1) in [("m.1 低音琶音", (360, 720)), ("m.2 低音琶音", (800, 1160))]:
    pts = blobs(x0,x1,300,445)
    cl = cluster(pts)
    print(f"\n{label}  x∈[{x0},{x1}]")
    for x,y,n in sorted(cl, key=lambda t:t[0]):
        nm, step = yname(y)
        print(f"  x={x:6.1f} y={y:6.1f} 音符≈{nm}  (距最上线 {step:+.1f} 半线, 宽{n})")
