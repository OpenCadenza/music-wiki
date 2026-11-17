import io

p = r"content\composers\bach\chorale\cadential-voice-clock-and-phase-decoupling.md"
s = io.open(p, encoding="utf-8").read()

old = """> **乐谱例证 4：待交付谱例定位（真实小节规范）**
> - **作品**：Johann Sebastian Bach - Chorale "Herzlich tut mich verlangen", BWV 153/5
> - **乐章与小节**：mm. 3–4（完全正格终止落音）
> - **编制与声部**：SATB 四部合唱（Soprano: GM 52, Alto: GM 52, Tenor: GM 52, Bass: GM 52）
> - **谱面特征**：第 4 小节下拍 a 小调终止落地和弦彻底省略五音 E，由低音 A2、次中音 A3、女高音 A4 构成三倍根音，中音 C4 构成单三音，完美展现线性声部导向对垂直和弦完整的压倒性优势
> - **交付状态**：已在 task-34 中立项，以真实作品小节规范文本占位，待后续谱例助手基于 Kern 谱 `chor021.krn` 编码交付"""

new = """> **乐谱例证 4：待交付谱例定位（真实小节规范）**
> - **作品**：Johann Sebastian Bach - Chorale "Herzlich tut mich verlangen", BWV 153/5
> - **乐章与小节**：mm. 3–4（完全正格终止落音）
> - **编制与声部**：SATB 四部合唱（Soprano: GM 52, Alto: GM 52, Tenor: GM 52, Bass: GM 52）
> - **谱面特征**：第 4 小节下拍 a 小调终止落地和弦彻底省略五音 E，由低音 A2、次中音 A3、女高音 A4 构成三倍根音，中音 C4 构成单三音，完美展现线性声部导向对垂直和弦完整的压倒性优势
> - **交付状态**：暂无（主控核验 S1 谱例中）

```lilypond title="BWV 153/5 第 3–4 小节" location="mm. 3–4"
\\version "2.26.0"
\\language "english"

\\header {
  title = "Chorale \\"Herzlich tut mich verlangen\\""
  subtitle = "BWV 153/5 (mm. 3–4)"
  composer = "Johann Sebastian Bach"
  tagline = ##f
}

global = {
  \\key a \\minor
  \\time 4/4
  \\tempo "Choral" 4 = 100
}

soprano = {
  \\global
  c''4 c''4 b'4 b'4 |
  a'2.\\fermata \\once \\omit Rest r4 |
}

alto = {
  \\global
  ds'4 e'4 fs'4 e'8 d'8 |
  c'2.\\fermata \\once \\omit Rest r4 |
}

tenor = {
  \\global
  a4 a4 a4 gs4 |
  a2.\\fermata \\once \\omit Rest r4 |
}

bass = {
  \\global
  fs4 e4 ds4 e4 |
  a,2.\\fermata \\once \\omit Rest r4 |
}

\\score {
  \\new StaffGroup <<
    \\new Staff \\with {
      instrumentName = "Soprano (GM 52)"
      midiInstrument = "choir aahs"
    } { \\soprano }
    \\new Staff \\with {
      instrumentName = "Alto (GM 52)"
      midiInstrument = "choir aahs"
    } { \\alto }
    \\new Staff \\with {
      instrumentName = "Tenor (GM 52)"
      midiInstrument = "choir aahs"
    } { \\clef "treble_8" \\tenor }
    \\new Staff \\with {
      instrumentName = "Bass (GM 52)"
      midiInstrument = "choir aahs"
    } { \\clef bass \\bass }
  >>
  \\layout { }
  \\midi { }
}
```"""

if old not in s:
    raise SystemExit("placeholder 4 not found")
s = s.replace(old, new, 1)
io.open(p, "w", encoding="utf-8", newline="\n").write(s)
print("ok, fences now:", s.count("```lilypond"), "placeholders:", s.count("待交付谱例定位"))
