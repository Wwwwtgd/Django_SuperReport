import pandas as pd


def dnf(df):
    df['检测日期'] = pd.to_datetime(df['检测日期'], format='%Y.%m.%d', errors='coerce')  # 将'检测日期'列转换为日期类型
    df['检测总长度(m)'] = pd.to_numeric(df['检测总长度(m)'], errors='coerce')  # 将'检测总长度(m)'列转换为数字类型
    # 按 '构件名称' 和 '焊缝名称' 分组
    grouped = df.groupby(['构件名称', '焊缝类型'], sort=False)

    # 创建新的列来标识分组，初始化
    df['分组编号'] = 0

    # 计算累计的 '检测总长度(m)'，并在累计值达到 150000 时分组
    for (component, weld), group in grouped:
        cumulative_length = 0
        group_index = 1  # 初始分组编号
        for idx, row in group.iterrows():
            cumulative_length += row['检测总长度(m)']

            # 判断是否超过 300000，超过则切换到新的分组
            if cumulative_length > 300000:
                group_index += 1
                cumulative_length = row['检测总长度(m)']  # 重置累计值为当前行的检测长度

            df.loc[idx, '分组编号'] = group_index

    # 再次按 '构件名称', '焊缝类型' 和 '分组编号' 进行分组
    return df.groupby(['构件名称', '焊缝类型', '分组编号'], sort=False)


