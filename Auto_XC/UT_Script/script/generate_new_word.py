from .add_res import *
from .check_and_change import *


def generate_new_word(b_no, document, second_page, group, save_path):
    document = add_res(document, second_page, b_no, group)  # 添加结果页后的 document 对象
    document.save(save_path)  # 保存文件
