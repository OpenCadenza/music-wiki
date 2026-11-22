# -*- coding: utf-8 -*-
"""Generate per-slug 来源与许可.md and an inventory JSON for the round-3 source report."""
import hashlib, json, re, zipfile
from pathlib import Path

BASE = Path(r"E:\github\music-wiki\.agents\worktrees\dsh-ee5c71d0-e1b5\local\workbench\scores\score-r3\downloads")
FETCHED = "2026-11-23 01:00 (Asia/Shanghai)"

MZ = "https://bitbucket.org/musedata/mozart/raw/master/nma/"
BH = "https://bitbucket.org/musedata/beethoven/raw/master/bhl/"
SQ = "https://raw.githubusercontent.com/OpenScore/StringQuartets/main/"
LD = "https://raw.githubusercontent.com/OpenScore/Lieder/main/"
HQ = "https://raw.githubusercontent.com/musedata/humdrum-haydn-quartets/master/kern/"
HS = "https://raw.githubusercontent.com/musedata/humdrum-haydn-symphonies/master/kern/"

LIC_MD = ("CCARH MuseData（斯坦福计算机辅助人文研究中心）；文件头含 (C) CCARH。"
          "许可为**学术研究用途**：可致谢引用、可用于核对，但**不得再发布/随教材分发原始数据**，"
          "商业衍生版、公开演出与录音亦受限（见 musedata 仓库 LICENSE.txt）。非 CC0。")
LIC_OSSQ = "CC0-1.0（OpenScore/StringQuartets 仓库 LICENSE.txt）；作品本身公有领域。原始贡献来自 MuseScore 社区，经 OpenScore 校订。"
LIC_OSLD = "CC0-1.0（OpenScore/Lieder 仓库 LICENSE.txt）；作品本身公有领域。"

# slug, filename, url, license, work, format, coverage, notes
ITEMS = [
 ("mozart-k550", "k550-mvt1.md2", MZ + "sym/k550/editions/public/score/mvt1.md2", LIC_MD,
  "Mozart, Symphony No. 40 in G minor, K.550 — Mvt 1", "MuseData md2",
  "第一乐章全（Molto allegro）；据 Neue Mozart-Ausgabe（NMA）转录，文件头注明 \"first version\"",
  "候选 #1 底本；亦可用于候选 #23（A/Bb 单簧管移调记谱）"),
 ("mozart-k467", "k467-mvt1.md2", MZ + "conc/k467/editions/public/score/mvt1.md2", LIC_MD,
  "Mozart, Piano Concerto No. 21 in C major, K.467 — Mvt 1", "MuseData md2",
  "第一乐章全（含乐队全奏段与钢琴段分谱行）", "候选 #19 ritornello 底本"),
 ("mozart-k467", "k467-mvt2.md2", MZ + "conc/k467/editions/public/score/mvt2.md2", LIC_MD,
  "Mozart, Piano Concerto No. 21 in C major, K.467 — Mvt 2", "MuseData md2",
  "第二乐章全（Andante）", "候选 #2（原 K.488 不可得，改 K.467 第二乐章）底本"),
 ("beethoven-op61", "op61-mvt1.md2", BH + "conc/violin/editions/public/score/mvt1.md2", LIC_MD,
  "Beethoven, Violin Concerto in D major, Op.61 — Mvt 1", "MuseData md2",
  "第一乐章全；据 Breitkopf & Haertel 全集转录，Fran Bennion 1996/2002",
  "候选 #19 第二底本（独奏—乐队交替）"),
 ("haydn-op76n3", "op76n3-02.krn", HQ + "op76n3-02.krn", LIC_MD,
  "Haydn, String Quartet in C major, Op.76 No.3 (Hob.III:77) — Mvt 2", "Humdrum **kern",
  "第二乐章（Poco adagio, cantabile, 变奏乐章）全", "候选 #4 主底本"),
 ("haydn-op76n3", "op76n3-03.krn", HQ + "op76n3-03.krn", LIC_MD,
  "Haydn, String Quartet in C major, Op.76 No.3 — Mvt 3", "Humdrum **kern",
  "第三乐章（Menuetto）全", "候选 #4 补充（舞曲乐章对照）"),
 ("haydn-op76n3", "op76n3-open-score.mxl", SQ + "scores/Haydn,_Joseph/String_Quartet_in_C_major,_Hob.III77,_Op.76_No.3/sq20428156.mxl", LIC_OSSQ,
  "Haydn, String Quartet in C major, Op.76 No.3 — 全曲 4 乐章", "MusicXML (MXL, MuseScore 导出)",
  "全曲四乐章", "候选 #4 第二来源（CC0，可公开引用的清版）"),
 ("haydn-sym104", "sym104a.krn", HS + "sym104a.krn", LIC_MD,
  "Haydn, Symphony No.104 in D major (London) — Mvt 1", "Humdrum **kern",
  "第一乐章（Adagio—Allegro）全，18 声部", "候选 #5 主底本"),
 ("haydn-sym104", "sym104b.krn", HS + "sym104b.krn", LIC_MD, "Haydn, Symphony No.104 — Mvt 2", "Humdrum **kern", "第二乐章（Andante）全", "候选 #5 补充"),
 ("haydn-sym104", "sym104c.krn", HS + "sym104c.krn", LIC_MD, "Haydn, Symphony No.104 — Mvt 3", "Humdrum **kern", "第三乐章（Menuetto: Allegro）全", "候选 #5 补充"),
 ("haydn-sym104", "sym104d.krn", HS + "sym104d.krn", LIC_MD, "Haydn, Symphony No.104 — Mvt 4", "Humdrum **kern", "第四乐章（Finale: Spiritoso）全", "候选 #5 补充"),
 ("haydn-seven-last-words", "haydn-op51-seven-last-words.mxl", SQ + "scores/Haydn,_Joseph/Die_Worte_des_Erlösers_am_Kreuze,_Hob.III50–56,_Op.51/sq19815031.mxl", LIC_OSSQ,
  "Haydn, Die sieben letzten Worte des Erlösers am Kreuze, Hob.III:50–56, Op.51（弦乐四重奏版）", "MusicXML (MXL)",
  "全曲：引子（Maestoso ed adagio）+ 7 首sonata + Il terremoto", "候选 #18 替换件底本（原 K.375/388 无编码源）"),
 ("mozart-k421", "mozart-k421.mxl", SQ + "scores/Mozart,_Wolfgang_Amadeus/String_Quartet_No.15_in_D_minor,_K.421417b_(Op._10,_No._2)/sq7294793.mxl", LIC_OSSQ,
  "Mozart, String Quartet No.15 in D minor, K.421/417b — 全曲 4 乐章", "MusicXML (MXL)", "全曲四乐章",
  "候选 #3 替换件底本（原《费加罗》重唱无机器可读源）"),
 ("schubert-d810", "schubert-d810.mxl", SQ + "scores/Schubert,_Franz/String_Quartet_in_D_minor,_D.810,_No.14_(\u201cDeath_and_the_Maiden\u201d)/sq7397765.mxl", LIC_OSSQ,
  "Schubert, String Quartet in D minor, D.810 No.14 (\"Death and the Maiden\") — 全曲 4 乐章", "MusicXML (MXL)",
  "全曲四乐章（含第二乐章 5 段变奏）", "候选 #6 替换件底本（原《未完成》交响曲无编码源）"),
 ("brahms-op51n1", "brahms-op51n1.mxl", SQ + "scores/Brahms,_Johannes/String_Quartet_No.1,_Op.51_No.1/sq7108150.mxl", LIC_OSSQ,
  "Brahms, String Quartet No.1 in C minor, Op.51 No.1 — 全曲 4 乐章", "MusicXML (MXL)", "全曲四乐章",
  "候选 #8 替换件底本（原 Symphony No.1 IV 无编码源）"),
 ("smetana-sq1", "smetana-sq1-from-my-life.mxl", SQ + "scores/Smetana,_Bedřich/String_Quartet_No.1/sq7483523.mxl", LIC_OSSQ,
  "Smetana, String Quartet No.1 in E minor \"Z mého života\"（我的一生）— 全曲 4 乐章", "MusicXML (MXL)", "全曲四乐章",
  "候选 #10 替换件底本（原肖邦叙事曲无编码源）"),
 ("dvorak-op96", "dvorak-op96-american.mxl", SQ + "scores/Dvořák,_Antonín/String_Quartet_No.12,_Op.96_(\u201cAmerican\u201d)/sq8885439.mxl", LIC_OSSQ,
  "Dvorak, String Quartet No.12 in F major, Op.96 (\"American\") — 全曲 4 乐章", "MusicXML (MXL)", "全曲四乐章",
  "候选 #11 替换件底本（原肖邦马祖卡无编码源）"),
 ("debussy-quartet", "debussy-op10.mxl", SQ + "scores/Debussy,_Claude/String_Quartet_in_G_minor,_Op.10/sq8661306.mxl", LIC_OSSQ,
  "Debussy, String Quartet in G minor, Op.10 — 全曲 4 乐章", "MusicXML (MXL)", "全曲四乐章",
  "候选 #13 主底本"),
 ("schubert-lieder", "D957-04-Standchen.mxl", LD + "scores/Schubert,_Franz/Schwanengesang,_D.957/04_Ständchen/lc5004835.mxl", LIC_OSLD,
  "Schubert, Schwanengesang D.957 No.4 \"Ständchen\"", "MusicXML (MXL)", "单曲全（人声+钢琴）",
  "候选 #7 底本之一（避开 D.328《魔王》）"),
 ("schubert-lieder", "D911-01-Gute-Nacht.mxl", LD + "scores/Schubert,_Franz/Winterreise,_D.911/01_Gute_Nacht/lc5015378.mxl", LIC_OSLD,
  "Schubert, Winterreise D.911 No.1 \"Gute Nacht\"", "MusicXML (MXL)", "单曲全（人声+钢琴）", "候选 #7 底本之一"),
 ("schubert-lieder", "D911-05-Der-Lindenbaum.mxl", LD + "scores/Schubert,_Franz/Winterreise,_D.911/05_Der_Lindenbaum/lc5016466.mxl", LIC_OSLD,
  "Schubert, Winterreise D.911 No.5 \"Der Lindenbaum\"", "MusicXML (MXL)", "单曲全（人声+钢琴）", "候选 #7 底本之一"),
 ("brahms-op91", "op91-1-Gestillte-Sehnsucht.mxl", LD + "scores/Brahms,_Johannes/2_Gesänge,_Op.91/1_Gestillte_Sehnsucht/lc6302395.mxl", LIC_OSLD,
  "Brahms, 2 Gesänge Op.91 No.1 \"Gestillte Sehnsucht\"（人声+中提琴+钢琴）", "MusicXML (MXL)", "单曲全（3 声部）",
  "候选 #9 替换件底本（原单簧管五重奏 Op.115 无编码源）"),
 ("brahms-op91", "op91-2-Geistliches-Wiegenlied.mxl", LD + "scores/Brahms,_Johannes/2_Gesänge,_Op.91/2_Geistliches_Wiegenlied/lc6320420.mxl", LIC_OSLD,
  "Brahms, 2 Gesänge Op.91 No.2 \"Geistliches Wiegenlied\"（人声+中提琴+钢琴）", "MusicXML (MXL)", "单曲全（3 声部）", "候选 #9 第二底本"),
 ("debussy-ariettes", "ariettes-1-Cest-lextase.mxl", LD + "scores/Debussy,_Claude/Ariettes_Oubliées/1_C\u2019est_l\u2019extase_langoureuse/lc5060910.mxl", LIC_OSLD,
  "Debussy, Ariettes oubliées No.1 \"C'est l'extase langoureuse\"", "MusicXML (MXL)", "单曲全（人声+钢琴）", "候选 #12 替换件底本（原钢琴前奏曲无编码源）"),
 ("debussy-ariettes", "ariettes-2-Il-pleure.mxl", LD + "scores/Debussy,_Claude/Ariettes_Oubliées/2_Il_pleure_dans_mon_coeur/lc5060918.mxl", LIC_OSLD,
  "Debussy, Ariettes oubliées No.2 \"Il pleure dans mon coeur\"", "MusicXML (MXL)", "单曲全", "候选 #12 底本"),
 ("debussy-ariettes", "ariettes-3-Lombre-des-arbres.mxl", LD + "scores/Debussy,_Claude/Ariettes_Oubliées/3_L\u2019ombre_des_arbres/lc5060924.mxl", LIC_OSLD,
  "Debussy, Ariettes oubliées No.3 \"L'ombre des arbres\"", "MusicXML (MXL)", "单曲全", "候选 #12 底本"),
 ("debussy-ariettes", "ariettes-4-Paysages-belges.mxl", LD + "scores/Debussy,_Claude/Ariettes_Oubliées/4_Paysages_belges._Chevaux_de_bois/lc5060932.mxl", LIC_OSLD,
  "Debussy, Ariettes oubliées No.4 \"Paysages belges: Chevaux de bois\"", "MusicXML (MXL)", "单曲全", "候选 #12 底本"),
 ("debussy-ariettes", "ariettes-5-Green.mxl", LD + "scores/Debussy,_Claude/Ariettes_Oubliées/5_Aquarelles_I._Green/lc5060938.mxl", LIC_OSLD,
  "Debussy, Ariettes oubliées No.5 \"Aquarelles I: Green\"", "MusicXML (MXL)", "单曲全", "候选 #12 底本"),
 ("debussy-ariettes", "ariettes-6-Spleen.mxl", LD + "scores/Debussy,_Claude/Ariettes_Oubliées/6_Aquarelles_II._Spleen/lc5060943.mxl", LIC_OSLD,
  "Debussy, Ariettes oubliées No.6 \"Aquarelles II: Spleen\"", "MusicXML (MXL)", "单曲全", "候选 #12 底本"),
]

# Dichterliebe 16 songs
DH = [("01_Im_wunderschönen_Monat_Mai","lc4976777"),("02_Aus_meinen_Tränen_sprießen","lc4976769"),
      ("03_Die_Rose,_die_Lilie","lc4976849"),("04_Wenn_ich_in_deine_Augen_seh\u2019","lc4978368"),
      ("05_Ich_will_meine_Seele_tauchen","lc4978373"),("06_Im_Rhein,_im_heiligen_Strome","lc4978379"),
      ("07_Ich_grolle_nicht","lc4978382"),("08_Und_wüssten\u2019s_die_Blumen","lc4978387"),
      ("09_Das_ist_ein_Flöten_und_Geigen","lc4978390"),("10_Hör\u2019_ich_das_Liedchen_klingen","lc5003150"),
      ("11_Ein_Jüngling_liebt_ein_Mädchen","lc4978393"),("12_Am_leuchtenden_Sommermorgen","lc4978395"),
      ("13_Ich_hab\u2019_im_Traum_geweinet","lc4978396"),("14_Allnächtlich_im_Traume","lc4978397"),
      ("15_Aus_alten_Märchen_winkt_es","lc4978398"),("16_Die_alten,_bösen_Lieder","lc4978400")]
for n, i in DH:
    safe = re.sub(r"[ ,\u2019]", "-", n)
    ITEMS.append(("schumann-dichterliebe", f"op48-{safe}.mxl",
                  LD + "scores/Schumann,_Robert/Dichterliebe,_Op.48/" + n + "/" + i + ".mxl", LIC_OSLD,
                  f"Schumann, Dichterliebe Op.48 No.{n[:2].lstrip('0')} — {n.split('_',1)[1].replace('_',' ')}",
                  "MusicXML (MXL)", "单曲全（人声+钢琴）", "候选 #20 替换件底本（原《狂欢节》无编码源）"))


def xml_facts(raw: bytes):
    txt = raw.decode("utf-8", "replace")
    parts = len(re.findall(r"<score-part\b", txt))
    # movement boundaries: measure number reset to 1 in first <part>
    first = txt.split("<part ")[1] if "<part " in txt else txt
    first = first.split("</part>")[0]
    nums = re.findall(r'<measure[^>]*number="(\d+)"', first)
    chunks = re.split(r'<measure[^>]*number="1"', first)
    mvmt_measures = [len(re.findall(r"<measure\b", "<measure" + c)) for c in chunks[1:]] or [len(nums)]
    return dict(parts=parts, total_measures=sum(mvmt_measures), movements=len(mvmt_measures),
                mvmt_measures=mvmt_measures)


inv = []
md_by_slug = {}
for slug, name, url, lic, work, fmt, coverage, note in ITEMS:
    p = BASE / slug / name
    if not p.exists():
        inv.append(dict(slug=slug, name=name, missing=True))
        continue
    b = p.read_bytes()
    sha = hashlib.sha256(b).hexdigest()
    rec = dict(slug=slug, name=name, bytes=len(b), sha256=sha, url=url, license=lic,
               work=work, format=fmt, coverage=coverage, note=note)
    if name.endswith(".mxl"):
        with zipfile.ZipFile(p) as z:
            sc = [n for n in z.namelist() if n.endswith((".xml", ".musicxml")) and "META-INF" not in n]
            rec["zip_members"] = z.namelist()
            raw = z.read(sc[0])
        rec.update(xml_facts(raw))
        rec["detected_title"] = (re.search(r"<movement-title>([^<]*)</movement-title>", raw.decode("utf-8", "replace")) or [None, ""])[1]
    elif name.endswith(".md2"):
        t = b.decode("utf-8", "replace")
        rec["wk"] = (re.search(r"WK#:(\S+)", t) or [None, None])[1]
        rec["mv"] = (re.search(r"MV#:(\S+)", t) or [None, None])[1]
        rec["barlines"] = len([l for l in t.splitlines() if l.startswith("=")])
        rec["source"] = (re.search(r"(Neue Mozart Augabe|Breitkopf[^\r\n]*)", t) or [None, None])[1]
        rec["copyright"] = (re.search(r"\(C\)[^\r\n]*", t) or [None, ""])[0]
        rec["muse2psv1"] = (re.search(r"@muse2psv1==(\S+)", t) or [None, None])[1]
    elif name.endswith(".krn"):
        t = b.decode("utf-8", "replace")
        rec["spines"] = t.count("**kern")
        rec["barlines"] = len([l for l in t.splitlines() if l.startswith("=")])
        rec["otl"] = (re.search(r"!!!OTL:\s*(.+)", t) or [None, ""])[1].strip()
        rec["sct1"] = (re.search(r"!!!SCT1:\s*(.+)", t) or [None, ""])[1].strip()
    inv.append(rec)
    md_by_slug.setdefault(slug, []).append(rec)

# write per-slug 来源与许可.md
for slug, recs in md_by_slug.items():
    lines = [f"# 来源与许可 —— {slug}", "",
             f"抓取时间：{FETCHED}；抓取人：`source-assistant-3`（music-wiki 第三轮 · 谱源盘点）。",
             "用途：为第三轮选题提供**可逐小节核对的机器可读底本**（扫描 PDF 不计入）。", "",
             "## 文件清单", "", "| 文件 | 字节 | SHA-256（前 16） | 格式 | 覆盖 |", "| --- | --- | --- | --- | --- |"]
    for r in recs:
        lines.append(f"| `{r['name']}` | {r['bytes']:,} | `{r['sha256'][:16]}` | {r['format']} | {r['coverage']} |")
    lines += ["", "## 取件 URL", ""]
    for r in recs:
        lines.append(f"- `{r['name']}`\n  - {r['work']}\n  - <{r['url']}>")
    lines += ["", "## 许可", ""]
    for lic in sorted({r["license"] for r in recs}):
        lines.append(f"- {lic}")
    lines += ["", "## 内容自证（本地实测）", ""]
    for r in recs:
        if "total_measures" in r:
            lines.append(f"- `{r['name']}`：MXL（内含 {len(r['zip_members'])} 个成员，含 META-INF/container.xml）；"
                         f"part 数 {r['parts']}，检测到 {r['movements']} 个乐章起算（每乐章小节数 {r['mvmt_measures']}），合计 {r['total_measures']} 小节；"
                         f"标题字段 \"{r['detected_title']}\"")
        elif "wk" in r:
            lines.append(f"- `{r['name']}`：MuseData md2，WK#{r['wk']} MV#{r['mv']}；barlines 记录 {r['barlines']}；"
                         f"源标注 \"{r['source']}\"；{r['copyright']}；muse2ps 版本串 `{r['muse2psv1']}`")
        elif "spines" in r:
            lines.append(f"- `{r['name']}`：Humdrum **kern，{r['spines']} 个 spine（声部/分谱行），barlines {r['barlines']}；"
                         f"OTL \"{r['otl']}\"，SCT1 \"{r['sct1']}\"")
    lines += ["", "## 备注", ""]
    for r in recs:
        if r.get("note"):
            lines.append(f"- {r['note']}")
    lines += ["", "> 说明：本目录文件仅作音乐维基内部核对底本，不再对外发布原始数据文件；"
                  "对外发布的是本项目自行编码的 LilyPond 谱例 + 引用声明。", ""]
    (BASE / slug / "来源与许可.md").write_text("\n".join(lines), encoding="utf-8")

Path(r"E:\github\music-wiki\.agents\worktrees\dsh-ee5c71d0-e1b5\local\workbench\scores\score-r3\inventory.json").write_text(
    json.dumps(inv, ensure_ascii=False, indent=1), encoding="utf-8")
print("files:", len(inv), "slugs:", len(md_by_slug))
print("missing:", [r["name"] for r in inv if r.get("missing")])
