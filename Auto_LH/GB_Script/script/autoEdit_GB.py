import pandas as pd


def auto_edit_gb(excel_path):
    data_all = pd.read_excel(excel_path, engine='openpyxl', sheet_name="总体信息", index_col=0, header=None).T.reset_index(drop=True)
    data_detail = pd.read_excel(excel_path, engine='openpyxl', sheet_name="钢板详细信息")
    report_num = data_all['报告数量'][0]
    print(data_all)
    print(data_detail)
    for i in range(report_num):
        print(f"正在处理第{i+1}份报告...")
