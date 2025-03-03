import datetime


def replace_the_dict(books1, replace_dict):
    # 总体信息
    replace_dict["这是工程名称"] = books1["工程名称"][0]
    replace_dict["这是委托单位"] = books1["委托单位"][0]
    # replace_dict["这是构件名称"] = "books1['构件名称'][0]"
    # replace_dict["这是检测部位"] = books1['检测部位'][0]
    # replace_dict["这是监理单位"] = books1['监理单位'][0]
    replace_dict["这是材质"] = books1["材质"][0]
    replace_dict["这是坡口形式"] = books1["坡口形式"][0]
    # replace_dict["这是检测数量"] = books1['检测数量'][0]
    replace_dict["这是检测时机"] = books1["检测时机"][0]
    replace_dict["这是焊接方式"] = books1["焊接方式"][0]
    replace_dict["这是检测比例"] = books1["检测比例"][0]
    replace_dict["这是热处理状态"] = books1["热处理状态"][0]
    replace_dict["这是工件温度"] = books1["工件温度"][0]
    replace_dict["这是表面状态"] = books1["表面状态"][0]
    replace_dict["这是仪器型号/编号"] = books1["仪器型号/编号"][0]
    replace_dict["这是探头规格"] = books1["探头规格"][0]
    replace_dict["这是耦合剂"] = books1["耦合剂"][0]
    replace_dict["这是表面补偿"] = books1["表面补偿"][0]
    replace_dict["这是对比试块"] = books1["对比试块"][0]
    replace_dict["这是标准试块"] = books1["标准试块"][0]
    # replace_dict["这是检测位置"] = books1["检测位置"][0]
    # replace_dict["这是扫查方式"] = books1["扫查方式"][0]
    replace_dict["这是检测灵敏度"] = books1["检测灵敏度"][0]
    replace_dict["这是检验标准"] = books1["检验标准"][0]
    replace_dict["这是母材检测结果"] = books1["母材检测结果"][0]


