from Auto_XC.UT_Script.script.generate_new_word import *
import pandas as pd
import copy
from .dnf import dnf
from .add_sign import *
from docx import Document
from .replace_the_dict import *
from multiprocessing import Pool
PATH_result = os.getcwd() + r'/Auto_XC/UT_Script/report_result/'
PATH_TEMPLATE = os.getcwd() + r'/Auto_XC/UT_Script/report_template/'


def process_report(params):
    no, ((component, weld, g), group), pt_doc, res_page, bk1, res_path = params
    document_copy = Document(pt_doc)
    total_length = str(group['检测总长度(mm)'].sum() / 1000) + " "  # 计算总长度
    final_date = group['检测日期'].max().strftime('%Y.%m.%d')
    qx_num = (group['结论'] == '不合格').sum()
    print(f'报告编号：{no:<10}' 
          f'构件名称: {component:<10}'
          f'焊缝名称: {weld:<10}'
          f'len: {len(group):<10}'
          f'总长度: {total_length:<10}'
          f'组：{g:<10}'
          f'不合格数量：{qx_num:<10}'
          )
    replace_eve_dict = {
        "这是构件名称": component,
        "这是检测部位": weld,
        "这是检测数量": total_length,
        "报告的日期": final_date,  # 替换字典
        "检测的结论": "检测结论合格"
    }
    if qx_num != 0:
        replace_eve_dict = {
            "检测的结论": f"发现 {qx_num} 处超标缺欠，其余焊缝检测结论合格"
        }

    # 调用生成报告函数
    b_no = bk1["报告编号"][0] + "-" + f"{no:03}"  # 报告编号
    save_path = res_path + "/" + str(b_no) + ".docx"  # 保存路径
    replace_eve_dict["这是报告的编号"] = b_no
    check_and_change(document_copy, replace_eve_dict)  # 替换第一页的内容
    generate_new_word(b_no, document_copy, res_page, group, save_path)
    print(f'保存路径: {save_path}')


def auto_edit_ut(book_path):
    path_all = os.path.dirname(book_path) + "/"
    pt_doc = path_all + str(os.path.basename(book_path).split('.')[0]) + ".docx"
    bk1 = pd.read_excel(book_path, engine='openpyxl', sheet_name="超声总体信息", index_col=0, header=None).T.reset_index(drop=True)  # 读取 excel 表, 获取总体信息
    bk2 = pd.read_excel(book_path, engine='openpyxl', sheet_name="超声原始记录")  # 读取 excel 表, 获取台账信息
    first_page = path_all + "A超声现场.docx"  # 第一页模板路径
    res_page = path_all + "A超声检测结果页.docx"  # 第二页模板路径

    res_path = PATH_result + bk1["报告编号"][0] + "/"
    if not os.path.exists(res_path):  # 如果文件夹路径不存在，则创建它
        os.makedirs(res_path)

    document = Document(first_page)  # 打开第一页
    replace_dict = {}  # 定义一个空字典来存储替换内容
    replace_the_dict(bk1, replace_dict)  # 设置第一页的替换字典
    check_and_change(document, replace_dict)  # 替换第一页的内容
    p_res = PATH_TEMPLATE + "示意图.png"
    add_syt(document, p_res)
    document.save(pt_doc)
    print(f'第一页模板报告已生成: {pt_doc}')
    grouped = dnf(bk2)

    # 准备传递给进程池的参数
    params_list = []
    for no, ((component, weld, g), group) in enumerate(grouped, 1):
        params_list.append((no, ((component, weld, g), group), pt_doc, res_page, bk1, res_path))

    # 使用 multiprocessing
    with Pool(processes=4) as pool:  # 这里可以根据 CPU 核心数调整进程数
        pool.map(process_report, params_list)
    print('所有报告生成完成！')
