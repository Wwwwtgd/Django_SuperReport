class GbParameter:
    def __init__(self, report_no="", sz_no="", lh="", ph="", gbh="", standard_no="", material="", thickness="", 
                 status="", z_status="", r_el_or_ul="", rm_value="", rm_limit="", re_value="", re_limit="", 
                 a_value="", a_limit="", bend_value="", bend_limit="", impact_value="", impact_limit="", c_value="", 
                 c_limit="", si_value="", si_limit="", mn_value="", mn_limit="", p_value="", p_limit="", s_value="", 
                 s_limit="", nb_value="", nb_limit="", v_value="", v_limit="", ti_value="", ti_limit="", al_value="", 
                 al_limit="", cr_value="", cr_limit="", ni_value="", ni_limit="", cu_value="", cu_limit="", mo_value="", 
                 mo_limit="", n_value="", n_limit=""):
        # 初始化所有字段
        self.report_no = report_no  # 报告控制编号
        self.sz_no = sz_no  # 样品编号
        self.lh = lh  # 炉号
        self.ph = ph  # 批号
        self.gbh = gbh  # 钢板号
        self.standard_no = standard_no  # 标准号
        self.material = material  # 材料
        self.thickness = thickness  # 厚度
        self.status = status  # 样品状态

        self.z_status = z_status  # Z 向状态
        self.r_el_or_ul = r_el_or_ul  # 上屈服或下屈服
        self.rm_value = rm_value  # 抗拉强度
        self.rm_limit = rm_limit  # 抗拉强度限值
        self.re_value = re_value  # 屈服强度
        self.re_limit = re_limit  # 屈服强度限值
        self.a_value = a_value  # 伸长率
        self.a_limit = a_limit  # 伸长率限值
        self.bend_value = bend_value  # 弯曲结果
        self.bend_limit = bend_limit  # 弯曲结果要求
        self.impact_value = impact_value  # 钢板材料冲击强度
        self.impact_limit = impact_limit  # 钢板材料冲击强度限值
        self.c_value = c_value  # 钢板材料 C 值
        self.c_limit = c_limit  # 钢板材料 C 值限值
        self.si_value = si_value  # 钢板材料 SI 值
        self.si_limit = si_limit  # 钢板材料 SI 值限值
        self.mn_value = mn_value  # 钢板材料 Mn 值
        self.mn_limit = mn_limit  # 钢板材料 Mn 值限值
        self.p_value = p_value  # 钢板材料 P 值
        self.p_limit = p_limit  # 钢板材料 P 值限值
        self.s_value = s_value  # 钢板材料 S 值
        self.s_limit = s_limit  # 钢板材料 S 值限值
        self.nb_value = nb_value  # 钢板材料 Nb 值
        self.nb_limit = nb_limit  # 钢板材料 Nb 值限值
        self.v_value = v_value  # 钢板材料 V 值
        self.v_limit = v_limit  # 钢板材料 V 值限值
        self.ti_value = ti_value  # 钢板材料 Ti 值
        self.ti_limit = ti_limit  # 钢板材料 Ti 值限值
        self.al_value = al_value  # 钢板材料 Al 值
        self.al_limit = al_limit  # 钢板材料 Al 值限值
        self.cr_value = cr_value  # 钢板材料 Cr 值
        self.cr_limit = cr_limit  # 钢板材料 Cr 值限值
        self.ni_value = ni_value  # 钢板材料 Ni 值
        self.ni_limit = ni_limit  # 钢板材料 Ni 值限值
        self.cu_value = cu_value  # 钢板材料 Cu 值
        self.cu_limit = cu_limit  # 钢板材料 Cu 值限值
        self.mo_value = mo_value  # 钢板材料 Mo 值
        self.mo_limit = mo_limit  # 钢板材料 Mo 值限值
        self.n_value = n_value  # 钢板材料 N 值
        self.n_limit = n_limit  # 钢板材料 N 值限值
