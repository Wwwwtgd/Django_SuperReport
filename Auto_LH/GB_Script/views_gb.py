import os
import zipfile
from io import BytesIO
import docx
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

path_all = 'Auto_LH/GB_Script/report_template/'


def get_form_data(request):
    if request.method == 'POST':
        form_data = request.POST
        project_name = form_data.get('project_name')  # 项目名称
        entrust_name = form_data.get('entrust_name')  # 委托单位
        sample_name = form_data.get('sample_name')  # 样品名称
        report_date = form_data.get('report_date')  # 报告日期
        number_of_report = form_data.get('number_of_report')  # 报告编号
        first_no = form_data.get('first_no')  # 首份报告编号
        come_date = form_data.get('come_date')  # 受样日期
        raw_no_type = form_data.getlist('raw_no_type')  # 原样编号类型
        standard = form_data.get('standard')  # 使用标准
        material = form_data.get('material')  # 材质
        thickness = form_data.get('thickness')  # 厚度
        status = form_data.get('status')  # 状态
        raw_no = form_data.get('raw_no')  # 原样编号
        print(first_no, project_name, entrust_name, sample_name, report_date, number_of_report, first_no, come_date,
              raw_no_type, standard, material, thickness, status, raw_no)
        
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=204)


def download_base_excel(request):
    file_path = path_all + 'list.xlsx'
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{file_path.split("/")[-1]}"'
        return response


def download_docx_files(request):
    zip_filename = "docx_files.zip"
    s = BytesIO()
    zf = zipfile.ZipFile(s, "w")
    for root, dirs, files in os.walk(path_all):
        for filename in files:
            if filename.endswith('.docx'):
                file_path = os.path.join(root, filename)
                zf.write(file_path, filename)
    zf.close()
    response = HttpResponse(s.getvalue(), content_type='application/zip')
    response['Content-Disposition'] = f'attachment; filename="{zip_filename}"'
    return response
