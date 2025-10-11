def once_change(document, replace_dict):
    # 确认字典只有一个键值对
    if len(replace_dict) != 1:
        raise ValueError("字典中必须只包含一个键值对")
    key, value = next(iter(replace_dict.items()))
    para = document.paragraphs
    for p in para:
        for run in p.runs:
            if key in run.text:
                run.text = run.text.replace(key, str(value))
                return
    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    for run in p.runs:
                        if key in run.text:
                            run.text = run.text.replace(key, str(value))
                            return


def same_check(para, replace_dict):
    replace_keys = set(replace_dict.keys())  # 将替换字典的键转换为集合，提高查找速度
    for p in para:
        for run in p.runs:
            original_text = run.text  # 获取当前 run 的原始文本
            new_text = original_text
            for key in replace_keys:
                if key in new_text:  # 只在文本中找到该 key 时才进行替换
                    new_text = new_text.replace(key, str(replace_dict[key]))
            if new_text != original_text:
                run.text = new_text


def check_and_change(document, replace_dict):
    same_check(document.paragraphs, replace_dict)
    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                same_check(cell.paragraphs, replace_dict)
    return document


def replace_header_text(document, old_text, new_text):
    # 遍历文档中的每个节（section）
    for section in document.sections:
        header = section.header  # 获取当前节的页眉
        for paragraph in header.paragraphs:
            if old_text in paragraph.text:
                # 替换文本
                inline_shapes = paragraph.runs
                inline_shapes[2].text = inline_shapes[2].text.replace(old_text, new_text)
