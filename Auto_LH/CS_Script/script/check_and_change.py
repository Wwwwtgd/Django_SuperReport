def same_check(para, replace_dict):
    replace_keys = set(replace_dict.keys())  # 将替换字典的键转换为集合，提高查找速度
    for p in para:
        for run in p.runs:
            for key in replace_keys:
                if key in run.text:
                    print(key + "-->" + str(replace_dict[key]))
                    run.text = run.text.replace(key, str(replace_dict[key]))


def check_and_change(document, replace_dict):
    same_check(document.paragraphs, replace_dict)
    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                same_check(cell.paragraphs, replace_dict)

    return document
