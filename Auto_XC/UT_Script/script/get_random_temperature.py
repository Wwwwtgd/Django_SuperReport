import random
import pandas as pd
from datetime import datetime


# 生成基于季节的随机温度
def get_random_temperature(date_str):
    # 解析日期
    date_obj = date_str
    month = date_obj.month

    if month == 1:
        temp_range = (6, 9)
    elif month == 2:
        temp_range = (8, 12)
    elif month == 3:
        temp_range = (13, 17)
    elif month == 4:
        temp_range = (18, 22)
    elif month == 5:
        temp_range = (23, 27)
    elif month == 6:
        temp_range = (27, 30)
    elif month == 7:
        temp_range = (31, 34)
    elif month == 8:
        temp_range = (31, 34)
    elif month == 9:
        temp_range = (21, 29)
    elif month == 10:
        temp_range = (21, 24)
    elif month == 11:
        temp_range = (15, 18)
    elif month == 12:
        temp_range = (8, 12)
    # 生成随机温度
    random_temp = random.randint(temp_range[0], temp_range[1])
    return random_temp
