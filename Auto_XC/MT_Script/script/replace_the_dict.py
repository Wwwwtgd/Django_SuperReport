import datetime


def replace_the_dict(books1, replace_dict):
    # 总体信息
    replace_dict["这是委托单位"] = books1["委托单位"][0]
    replace_dict["这是工程名称"] = books1["工程名称"][0]
    replace_dict["这是材质"] = books1["材质"][0]
    replace_dict["这是反差剂"] = books1["反差增强剂"][0]
    replace_dict["这是检测时机"] = books1["检测时机"][0]
    replace_dict["这是磁悬液"] = books1["磁悬液类型"][0]
    if type(books1["检测比例"][0]) == str:
        replace_dict["这是检测比例"] = books1["检测比例"][0]
    else:
        bl = books1["检测比例"][0]
        replace_dict["这是检测比例"] = f"{bl:.0%}"
    replace_dict["这是仪器型号"] = books1["仪器型号/编号"][0]
    replace_dict["这是施加方法"] = books1["施加方法"][0]
    replace_dict["这是磁化电流"] = books1["磁化电流/提升力"][0]
    replace_dict["这是表面状况"] = books1["表面状况"][0]
    replace_dict["这是磁化方法"] = books1["磁化方法"][0]
    replace_dict["这是磁化时间"] = books1["磁化时间"][0]
    replace_dict["这是检验标准"] = books1["检验标准"][0]
    replace_dict["这是验收标准"] = books1["验收标准"][0]
    replace_dict["这是灵敏度"] = books1["灵敏度试片"][0]
    replace_dict["这是观察环境"] = books1["观察环境"][0]


