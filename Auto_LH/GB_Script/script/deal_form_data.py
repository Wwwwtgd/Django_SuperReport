from Auto_LH.GB_Script.script.GbParameter import GbParameter
import pandas as pd
import os
from datetime import datetime
current_time = datetime.now()
PATH_template = os.getcwd() + r'/Auto_LH/GB_Script/report_template/'


def deal_form_data(form_data):
    # 统一的信息
    project_name = form_data.get('project_name')  # 项目名称
    entrust_name = form_data.get('entrust_name')  # 委托单位
    manufacturer = form_data.get('manufacturer')  # 制造商
    sample_name = form_data.get('sample_name')  # 样品名称
    jl_open = form_data.get('jl_open')  # 监理单位
    jz_open = form_data.get('jz_open')  # 见证单位
    jz_r = form_data.get('jz_r_open')  # 见证人
    qy_open = form_data.get('qy_open')  # 取样单位
    qy_r = form_data.get('qy_open')  # 取样人
    report_date = form_data.get('report_date')  # 报告日期
    come_date = form_data.get('come_date')  # 受样日期
    number_of_report = int(form_data.get('number_of_report'))  # 报告数量 -
    # 每份钢板的信息
    first_no = form_data.get('first_no')  # 首份报告编号 -
    raw_no_type = form_data.getlist('raw_no_type')  # 原样编号类型 可能是炉号、批号、钢板号中的一个或多个 -
    chemical = form_data.getlist('chemical')  # 检测元素复选框选中的值，可能是多个元素的组合 -
    z_open = form_data.getlist('open')  # Z 向性能开关的值，是on或off -
    z_status = form_data.getlist('z_status')  # 需要查看 Z 向性能开关状态，再决定获不获取这个值
    lh = form_data.getlist('lh')  # 炉号输入框的值
    ph = form_data.getlist('ph')  # 批号输入框的值
    gbh = form_data.getlist('gbh')  # 钢板号输入框的值
    standard = form_data.getlist('standard')  # 验收标准下拉框选中的值
    material = form_data.getlist('material')  # 材质输入框的值
    thickness = form_data.getlist('thickness')  # 规格输入框的值
    status = form_data.getlist('status')  # 样品状态下拉框选中的值

    # 创建一个空的 DataFrame 用于"all_same_info"表
    all_same_info_columns = ["项目名称", "委托单位", "制造商", "样品名称", "监理单位", "见证单位",
                             "见证人", "取样单位", "取样人", "报告日期", "受样日期", "报告数量"]
    all_same_info_data = [[project_name, entrust_name, manufacturer, sample_name, jl_open, jz_open,
                           jz_r, qy_open, qy_r, report_date, come_date, number_of_report]]
    # 先创建原始数据框
    all_same_info_df = pd.DataFrame(all_same_info_data, columns=all_same_info_columns)
    # 转置 all_same_info_df 数据
    all_same_info_df_transposed = all_same_info_df.transpose()  # 转置 DataFrame
    # 将原列名转为 '字段' 列，将数据放入 '值' 列
    all_same_info_df_transposed.reset_index(inplace=True)
    all_same_info_df_transposed.columns = ['字段', '值']
    # 创建一个空的 DataFrame 用于"GB_info"表
    gb_info_columns = [
        "报告控制编号", "样品编号", "炉号", "批号", "钢板号"
    ]
    gb_info_df = pd.DataFrame(columns=gb_info_columns)
    path_template = PATH_template + '钢板的信息' + str(current_time.strftime("%Y年%m月%d日%H点%M分%S秒")) + '.xlsx'
    # 创建一个 Excel 文件，并将两个表格写入其中
    with pd.ExcelWriter(path_template, engine='xlsxwriter') as writer:
        # 将数据框写入各个表
        all_same_info_df_transposed.to_excel(writer, sheet_name='all_same_info', index=False)
        gb_info_df.to_excel(writer, sheet_name='GB_info', index=False)

    gb_data = []  # 存放 GbParameter 对象 ，钢板全部参数
    replace_dict = {}
    for i in range(number_of_report):
        now_number = int(first_no[-3:]) + i
        # 报告编号
        first_no_i = first_no[:-3] + str(int(first_no[-3:]) + i).zfill(3) if first_no != '/' else '/'
        replace_dict['报告编号'] = first_no_i
        # 炉号/ 批号/ 钢板号
        raw_no_map = {'炉号': lh[i], '批号': ph[i], '钢板号': gbh[i]}
        for key in raw_no_type:
            replace_dict[key] = str(raw_no_map.get(key))
        # 标准号

        # 样品编号
        sample_no = 'SZ-GB-' + str(now_number).zfill(2)

        # gb_obj = GbParameter(first_no_i, lh[i], ph[i], gbh[i], manufacturer, sample_name, report_date, come_date, chemical, z_open, z_status, standard, material, thickness, status)
