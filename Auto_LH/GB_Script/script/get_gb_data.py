from Auto_LH.GB_Script.script.GbParameter import GbParameter
import pandas as pd
import re
import numpy as np
import random


def get_detect_rd(mid, fd, add_value):
    if add_value == '/' or add_value == 'nan':
        return '/'
    add_value = re.findall(r'\d+', str(add_value))
    if len(add_value) == 1:
        if (mid - fd) < int(add_value[0]):
            return "范围不符合要求"
    elif len(add_value) == 2:
        if (mid - fd) < int(add_value[0]) or (mid + fd) > int(add_value[1]):
            return "范围不符合要求"
    else:
        return '要求错误'
    # 设置均值和标准差
    mean = mid  # 均值取中间值
    std = fd / 3  # 标准差可以根据数据的范围设置，6倍标准差基本覆盖99%的数据
    # 生成一个正态分布的随机数，并裁剪到 [start, End ] 范围
    value = np.random.normal(mean, std)
    # 将随机数限制在 [start, end ] 之间
    value = np.clip(value, mid + fd, mid - fd)
    return int(value)


def get_hx_value(mid, fd, hx_condition):
    if hx_condition == '/':
        return '/'
    # 解析 hx_condition 字符串，获取 hx_value
    match = re.findall(r'-?\d+\.\d+|-?\d+', hx_condition)
    if len(match) == 1:
        if (mid + fd) > float(match[0]):
            return "范围不符合要求"
        else:
            hx_values = [random.uniform(0, float(match[0])) for _ in range(3)]
    elif len(match) == 2:
        if (mid - fd) < float(match[0]) or (mid + fd) > float(match[1]):
            return "范围不符合要求"
        else:
            hx_values = [random.uniform(float(match[0]), float(match[1])) for _ in range(3)]
    else:
        return '要求错误'
    return '、'.join([f"{float(value):.3f}" for value in hx_values])


# 定义一个函数来判断给定的厚度是否符合范围
def is_thickness_in_range(thickness_condition, thickness_value):
    # 使用正则表达式解析范围
    match = re.findall(r'\d+', thickness_condition)
    if len(match) == 2:
        if int(match[0]) < thickness_value <= int(match[1]):
            return True
    elif len(match) == 1:
        if thickness_value <= int(match[0]):
            return True
    return False


def get_gb_data(gb_param):
    # 读取Excel文件
    df = pd.read_excel(r'G:\work\data\规范\钢板与焊丝标准整理\材质数据库.xlsx')

    # 筛选数据
    filtered_df = df[
        (df['标准'] == gb_param.standard_no) &
        (df['材质'] == gb_param.material) &
        (df['工艺'] == gb_param.status)
        ]
    # 获取 '板厚' 列的所有唯一值
    for index, row in filtered_df.iterrows():
        thickness_condition = row['板厚']
        if is_thickness_in_range(thickness_condition, gb_param.thickness):
            gb_param.r_el_or_ul = row['屈服']
            gb_param.rm_value = get_detect_rd(560, 50, row['抗拉强度'])
            gb_param.rm_limit = row['抗拉强度']
            gb_param.re_value = get_detect_rd(402, 20, row['屈服强度'])
            gb_param.re_limit = row['屈服强度']
            scl = get_detect_rd(28, 5, row['伸长率'])
            if isinstance(scl, str):
                gb_param.a_value = scl
            else:
                gb_param.a_value = scl + random.choice([0, 0.5])
            gb_param.a_limit = row['伸长率']
            if gb_param.z_limit != '/':
                z_vn = get_detect_rd(68, 3, gb_param.z_limit)
                if isinstance(z_vn, str):
                    gb_param.z_value = z_vn
                else:
                    z_vns = [get_detect_rd(68, 3, gb_param.z_limit) + random.choice([0, 0.5]) for _ in range(3)]
                    gb_param.z_value = '、'.join(map(str, z_vns))
            gb_param.bend_value = str("无裂纹")
            cj = get_detect_rd(32, 120, row['冲击/J'])
            if isinstance(cj, str):
                gb_param.impact_value = cj
            else:
                cjs = [get_detect_rd(32, 120, row['冲击/J']) + random.choice([0, 0.5]) for _ in range(3)]
                gb_param.impact_value = '、'.join(map(str, cjs))
            gb_param.impact_limit = str(row['冲击/J']) + "J" + "(" + str(row['温度/℃']) + "℃)"
            gb_param.c_value = get_hx_value(0.8, 0.002, row['C'])
            gb_param.c_limit = row['C']
            gb_param.si_value = get_hx_value(0.5, 0.001, row['Si'])
            gb_param.si_limit = row['Si']
            gb_param.mn_value = get_hx_value(1.3, 0.006, row['Mn'])
            gb_param.mn_limit = row['Mn']
            gb_param.p_value = get_hx_value(0.015, 0.002, row['P'])
            gb_param.p_limit = row['P']
            gb_param.s_value = get_hx_value(0.003, 0.002, row['S'])
            gb_param.s_limit = row['S']
            gb_param.nb_value = get_hx_value(0.03, 0.002, row['Nb'])
            gb_param.nb_limit = row['Nb']
            gb_param.v_value = get_hx_value(0.003, 0.002, row['V'])
            gb_param.v_limit = row['V']
            gb_param.ti_value = get_hx_value(0.8, 0.002, row['Ti'])
            gb_param.ti_limit = row['Ti']
            gb_param.al_value = get_hx_value(0.8, 0.002, row['Als'])
            gb_param.al_limit = row['Als']
            gb_param.cr_value = get_hx_value(0.2, 0.002, row['Cr'])
            gb_param.cr_limit = row['Cr']
            gb_param.ni_value = get_hx_value(0.1, 0.002, row['Ni'])
            gb_param.ni_limit = row['Ni']
            gb_param.cu_value = get_hx_value(0.3, 0.002, row['Cu'])
            gb_param.cu_limit = row['Cu']
            gb_param.mo_value = get_hx_value(0.8, 0.002, row['Mo'])
            gb_param.mo_limit = row['Mo']
            gb_param.n_value = get_hx_value(0.8, 0.002, row['N'])
            gb_param.n_limit = row['N']

    return gb_param
