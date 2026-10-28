import json, os, re
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
    lines=["# 阅读资料库","","本库供音乐学者发现、阅读和调用资料。预备轮与正式轮新增材料同等可用；资料卡和助手概述不能代替实际阅读。原件保存在相邻的 origin_resources，正文文章另在 content 中维护。","","## 先从这些入口阅读","","- [全部来源与文本入口](catalog/parts/text/index.md)：26类来源，含教材、论文、背景、乐器资料、标注与谱源。","- [HTML整理正文](text/organized-html/README.md)：去掉网站导航的论文、介绍与乐器资料，保留原网页映射。","- [OCR 文献与图像目录](catalog/ocr-conversions.md)：真实转换状态、页数、Markdown与原件链接。","- [OCR验收与限制](catalog/parts/ocr/index.md)：物理页记录核对、图像引用检查及空文字结果。","- [已解包谱源入口](scores/source-packages/README.md)：Kern与DCML原生谱文件。","- [完整加工索引](catalog/index.json)：机器可读的来源与处理状态。","","## 当前预备整理","","| 内容 | 数量／状态 |","| --- | --- |",f"| 来源卡 | {count.get('sources',0)} |",f"| 保留的HTML／文本副本 | {count.get('readable_text_copies',0)} |",f"| HTML整理正文 | {count.get('cleaned_html_documents',0)} |",f"| 关联图像 | {count.get('associated_image_assets',0)} |",f"| OMT旧版文本与图像抽取项 | {text.get('omt',{}).get('count',0)} |",f"| 与官方旧版源码对应的既有OMT Markdown | {text.get('existing_omt_comparison',{}).get('matched',0)} |",f"| DCML表格与元数据 | {text.get('dcml',{}).get('count',0)} |",f"| 已解包机器可读谱文件 | {count.get('machine_readable_score_files',0)} |",f"| OCR作业完成 | {statuses.get('converted_readable',0)+statuses.get('converted_image_only',0)} / {len(rows)} |",f"| 有OCR文字的文档 | {statuses.get('converted_readable',0)} |",f"| 仅原件图像可读（OCR文字为空） | {statuses.get('converted_image_only',0)} |","","数量描述实际文件和转换状态，不代表全文已被学者阅读。目录／摘要、失败／未缓存、仅部分取得均在来源卡说明。","","## 阅读与谱例","","OMT教材、论文、版本导言与乐器资料可以直接启发选题。标注数据需要结合数据字典和原谱；它们不是唯一正确的音乐分析。Kern、ABC、MusicXML、LilyPond与原谱图像的入口见来源卡和谱包目录。","","PDF／图片由用户指定 EverythingMarkdown（PaddleOCR-VL-1.6）转换。原谱OCR保留文字和图像，不保证识别音符；需要代码时查可靠谱源或处理目标片段。","","## 已知缺口","","- 历史收集偏重贝多芬，不代表正式轮优先；学者可从其他材料选题，再由资料助手按需补充。","- OMT2导出、部分来源下载和未缓存全文的历史缺口，见各来源卡。","- 部分HTML内文图像不在原库，整理正文明确标注缺失；这类材料不能冒称图文齐全，正式研究可按需补图。","- OMT旧版仍有一条 sonata.html 指向未取得目标；PDMX README的PDMX.png未取得，保持缺失状态。","- 大型OpenScore包保留目录，大型PDMX归档不盲目展开；已知原件始终可从原始库追查。","- OCR作业完成不保证文字识别。op98-autograph-page-002.jpg返回文字为空，保留服务输出并提供原图阅读入口，标为converted_image_only。","","旧Agent生成文章、自编模型和历史日志不在默认学术阅读入口中。"]
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
    # Merge OCR reading links into the same source cards after both workers finish.
    for card in (CAT/"parts/text/sources").glob("*.md"):
        related=[r for r in rows if len(Path(r["source_path"]).parts)>1 and Path(r["source_path"]).parts[1]==card.stem]
        body=card.read_text(encoding="utf-8")
        body=re.sub(r"\n<!-- unified-ocr:start -->[\s\S]*?<!-- unified-ocr:end -->\n?", "\n", body)
        if related:
            block=["", "<!-- unified-ocr:start -->", "## OCR 阅读副本", "", "以下页数是PDF物理页数；转换可读不表示学者已读。原谱图像的OCR文字不能充当音符编码。", ""]
            for row in related:
                links=[]
                for output in row.get("outputs",[]):
                    if output.get("markdown"):
                        target=os.path.relpath(ROOT/output["markdown"],card.parent).replace(chr(92),'/')
                        links.append(f"[{output.get('page_range','Markdown')}]({target})")
                block.append(f"- **{Path(row['source_path']).name}**（{row.get('page_count','')}页）— {row['status']}；{'、'.join(links) or '尚无可读副本'}")
            block += ["", "<!-- unified-ocr:end -->", ""]
            body=body.rstrip()+"\n"+"\n".join(block)
        card.write_text(body,encoding="utf-8")
    print(json.dumps({"sources":count.get("sources",0),"ocr_statuses":statuses,"ocr_documents":len(rows)},ensure_ascii=False))
if __name__=="__main__": main()
