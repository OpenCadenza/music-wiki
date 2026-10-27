import json, os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
LOCAL=ROOT/"local"
RES=LOCAL/"resources"
CAT=RES/"catalog"
TEXT=CAT/"parts/text/index.json"
def rel_link(p): return os.path.relpath(p,RES).replace("\\","/")
def main():
    text=json.loads(TEXT.read_text(encoding="utf-8")) if TEXT.exists() else {}
    rows=[]
    for meta in sorted((RES/"text/ocr").rglob("conversion.json")):
        row=json.loads(meta.read_text(encoding="utf-8"))
        row["metadata"]=rel_link(meta)
        rows.append(row)
    statuses={}
    for row in rows: statuses[row["status"]]=statuses.get(row["status"],0)+1
    summary={"updated_for":"2026-10-28预备轮","scope":"资料可发现与可阅读，不表示学者已实际阅读","original_source_count":text.get("counts",{}).get("sources",0),"text_summary":text.get("counts",{}),"omt_summary":{k:v for k,v in text.get("omt",{}).items() if k!="copies"},"dcml_summary":text.get("dcml",{}),"archives":text.get("archives",[]),"ocr_statuses":statuses,"ocr_documents":rows}
    CAT.mkdir(parents=True,exist_ok=True)
    (CAT/"index.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    count=text.get("counts",{})
    lines=["# 阅读资料库","","本库供音乐学者发现、阅读和调用资料。预备轮与正式轮新增材料同等可用；资料卡和助手概述不能代替实际阅读。原件保存在相邻的 origin_resources，正文文章另在 content 中维护。","","## 先从这些入口阅读","","- [全部来源与文本入口](catalog/parts/text/index.md)：26类来源，含教材、论文、背景、乐器资料、标注与谱源。","- [OCR 文献与图像目录](catalog/ocr-conversions.md)：真实转换状态、页数、Markdown与原件链接。","- [完整加工索引](catalog/index.json)：机器可读的来源与处理状态。","","## 当前预备整理","","| 内容 | 数量／状态 |","| --- | --- |",f"| 来源卡 | {count.get('sources',0)} |",f"| 原始HTML等文本阅读副本 | {count.get('readable_text_copies',0)} |",f"| 关联图像 | {count.get('associated_image_assets',0)} |",f"| OMT旧版文本与图像抽取项 | {text.get('omt',{}).get('count',0)} |",f"| 与官方旧版源码对应的既有OMT Markdown | {text.get('existing_omt_comparison',{}).get('matched',0)} |",f"| DCML表格与元数据 | {text.get('dcml',{}).get('count',0)} |",f"| OCR成功文档 | {statuses.get('converted_readable',0)} / {len(rows)} |","","数量描述实际文件和转换状态，不代表全文已被学者阅读。目录／摘要、失败／未缓存、仅部分取得均在来源卡说明。","","## 阅读与谱例","","OMT教材、论文、版本导言与乐器资料可以直接启发选题。标注数据需要结合数据字典和原谱；它们不是唯一正确的音乐分析。Kern、ABC、MusicXML、LilyPond与原谱图像的入口见来源卡和谱包目录。","","PDF／图片由用户指定 EverythingMarkdown（PaddleOCR-VL-1.6）转换。原谱OCR保留文字和图像，不保证识别音符；需要代码时查可靠谱源或处理目标片段。","","## 已知缺口","","- OMT2导出、部分来源下载和未缓存全文的历史缺口，见各来源卡。","- OMT旧版仍有一条 sonata.html 指向未取得目标；PDMX README的PDMX.png未取得，保持缺失状态。","- 大型OpenScore包保留目录，大型PDMX归档不盲目展开；已知原件始终可从原始库追查。","- OCR进行中或未转换的文献不能标为可读；完成后用本地refresh_resource_index.py刷新本入口。","","旧Agent生成文章、自编模型和历史日志不在默认学术阅读入口中。"]
    (RES/"README.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    lines=["# OCR 文献与图像","","模型：PaddleOCR-VL-1.6，工具：用户指定 EverythingMarkdown。以下状态只表示转换是否完成，不能冒充音乐学者已经阅读。","","| 原件 | 页数 | 状态 | 阅读副本 |","| --- | ---: | --- | --- |"]
    for row in rows:
        src=row["source_path"]
        origin=LOCAL/"origin_resources"/src
        source=f"[{Path(src).name}]({os.path.relpath(origin,CAT).replace(chr(92),'/')})"
        outputs=row.get("outputs",[])
        links=[]
        for output in outputs:
            name=output.get("markdown")
            if name:
                p=ROOT/name
                links.append(f"[{output.get('page_range','Markdown')}]({os.path.relpath(p,CAT).replace(chr(92),'/')})")
        lines.append(f"| {source} | {row.get('page_count','')} | {row.get('status','')} | {'、'.join(links) or '尚无可读副本'} |")
    lines+=["","源SHA、模型、页范围、转换日志和图像目录见各文档同目录conversion.json；错误与未尝试状态如实保留。"]
    (CAT/"ocr-conversions.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    print(json.dumps({"sources":count.get("sources",0),"ocr_statuses":statuses,"ocr_documents":len(rows)},ensure_ascii=False))
if __name__=="__main__": main()
