from openpyxl.styles import Alignment, PatternFill


def write_gb_info_to_excel(gb_param, df_detailed, insert_row_index):
    # 将 gb_param 转换为字典
    gb_param_dict = {
        "控制编号": gb_param.report_no,
        "样品编号": gb_param.sz_no,
        "炉号": gb_param.lh,
        "批号": gb_param.ph,
        "钢板号": gb_param.gbh,
        "验收的依据": gb_param.standard_no,
        "材质": gb_param.material,
        "规格": gb_param.thickness,
        "样品状态": gb_param.status,
        "生产厂家": gb_param.manufacturer,
        "受样日期": gb_param.come_date,
        "理化日期": gb_param.detect_date_lh,
        "化学日期": gb_param.detect_date_hx,
        "报告日期": gb_param.report_date,
        "上下屈服": gb_param.r_el_or_ul,
        "抗拉强度": gb_param.rm_value,
        "抗拉要求": gb_param.rm_limit,
        "屈服强度": gb_param.re_value,
        "屈服要求": gb_param.re_limit,
        "伸长率": gb_param.a_value,
        "伸长要求": gb_param.a_limit,
        "Z向值": gb_param.z_value,
        "Z要求": gb_param.z_limit,
        "弯曲": gb_param.bend_value,
        "冲击结果": gb_param.impact_value,
        "冲击要求": gb_param.impact_limit,
        "C元素": gb_param.c_value,
        "C要求": gb_param.c_limit,
        "Si元素": gb_param.si_value,
        "Si要求": gb_param.si_limit,
        "Mn元素": gb_param.mn_value,
        "Mn要求": gb_param.mn_limit,
        "P元素": gb_param.p_value,
        "P要求": gb_param.p_limit,
        "S元素": gb_param.s_value,
        "S要求": gb_param.s_limit,
        "Nb元素": gb_param.nb_value,
        "Nb要求": gb_param.nb_limit,
        "V元素": gb_param.v_value,
        "V要求": gb_param.v_limit,
        "Ti元素": gb_param.ti_value,
        "Ti要求": gb_param.ti_limit,
        "Al元素": gb_param.al_value,
        "Al要求": gb_param.al_limit,
        "Cr元素": gb_param.cr_value,
        "Cr要求": gb_param.cr_limit,
        "Ni元素": gb_param.ni_value,
        "Ni要求": gb_param.ni_limit,
        "Cu元素": gb_param.cu_value,
        "Cu要求": gb_param.cu_limit,
        "Mo元素": gb_param.mo_value,
        "Mo要求": gb_param.mo_limit,
        "N元素": gb_param.n_value,
        "N要求": gb_param.n_limit,
    }

    header = [cell.value for cell in df_detailed[1]]  # 读取第一行的表头
    # **根据表头名称匹配列，并写入数据**
    for col_index, col_name in enumerate(header, start=1):  # 遍历表头
        if col_name in gb_param_dict:  # 如果新数据包含这个列
            df_detailed.cell(row=insert_row_index, column=col_index, value=gb_param_dict[col_name])
    return df_detailed
