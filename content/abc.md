<!-- music-kb:page {"id": "page.92014569ee9d43f78899b681df271ccd"} -->
<!-- knowledge: operation.abc -->
# ABC 写谱与检查
直接写 ABC 2.1 单文件。每首/乐章用 X:，明确 T:/M:/L:/K:，V: 声部声明与切换一致。按 L: 逐拍计时，核对连音、延音、休止、反复及结尾；大写音与小写音、逗号/撇号控制八度，临时变音传播须检查。
ABC 变音使用 ^ / _ / =，不能混入 LilyPond 的 bes、fis 等名称。例如 K:Dm 中 B/b 默认降B；需显式记谱用 _B/_b。不能把 ABC 的小写 c 与大写 C 当成同一八度。
所有伴奏用音符写出；禁止 gchordon、drumon、droneon 等自动发声，不用和弦名代替伴奏，不隐藏声部。MIDI program 音色设置可以使用。
首小节可能是弱起，尾小节可补齐；显式解释两者关系，不任意少拍或超拍。编译器可能接受错拍，审稿需复核。多个 X: 全部写完并验证。多声部编写尽量采用易定位的整段 V: 块，局部替换覆盖全部受影响声部。

## 自编示例：按 L: 核对八度和弱起

本库自编教学例，CC BY-SA 4.0；不是历史作品摘录。语法依据 [ABC 2.1 标准](https://abcnotation.com/wiki/abc:standard:v2.1) 的 pitch、note lengths、meter、key、voices 相关小节；没有复制标准正文。

<!-- music-kb:block {"id": "abc.e854c580ba7a46db93275c69b4698abf", "language": "abc"} -->
```abc
X:1
T:Pickup and register teaching example
M:4/4
L:1/8
K:C
G2 | C2 D2 E2 F2 | G2 A2 B2 c2 | c4 z2 |]
```

开头 G2 是四分音符弱起；末小节 c4 z2 为三拍，二者合计四拍。第二个完整小节末尾 c 是 C5，前面的 C 是 C4。`L:1/8` 下 C2 为四分音符，不能按字面数字2解读为二分音符。

示例只检验记谱关系，不证明旋律质量。脚本分析时声明弱起一拍；完整小节数与记谱小节标签要区分。多声部、变拍与反复需要各自核对，不能从这个单声部短例推断。
