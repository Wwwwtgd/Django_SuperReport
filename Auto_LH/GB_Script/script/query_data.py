from GbParameter import GbParameter
import pandas as pd
import os


# Function to query data based on GbParameter object
def query_data(gb_param, dataframe):
    # Filter the dataframe based on the provided attributes
    filtered = dataframe[(dataframe['标准'] == gb_param.standard_no) &
                         (dataframe['材质'] == gb_param.material) &
                         (dataframe['板厚'] == gb_param.thickness) &
                         (dataframe['工艺'] == gb_param.status)]

    # Check if any rows match the criteria
    if not filtered.empty:
        return filtered.to_dict(orient='records')  # Return matching rows as a list of dictionaries
    else:
        return None  # No match found


# Example usage with loaded data (sheet_data):
gb_param = GbParameter(report_no=None, sz_no=None, lh=None, ph=None, gbh=None,
                       standard_no='GB/T 714-2015', material='Q345qC', thickness='t ≤ 50', status='AR')
# 提供 Excel 文件路径
file_path = fr"{os.getcwd().split(':')[0]}:/work/data/规范/钢板与焊丝标准整理/材质数据库.xlsx"  # 替换为实际路径

# 读取 Excel 文件，加载指定的工作表（如 Sheet1）
sheet_data = pd.read_excel(file_path, sheet_name="Sheet1")
result = query_data(gb_param, sheet_data)
print(result)
