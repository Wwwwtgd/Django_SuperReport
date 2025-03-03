import os
import zipfile
from io import BytesIO
from django.http import JsonResponse, HttpResponse
from Auto_LH.GB_Script.script.deal_form_data import deal_form_data
PATH_template = os.getcwd() + r'/Auto_LH/GB_Script/report_template/'


def get_form_gb_data(request):
    if request.method == 'POST':
        form_data = request.POST
        res = deal_form_data(form_data)  # 处理表单数据
        print(form_data)
        return HttpResponse(status=204)
    return HttpResponse(status=404)


def download_gb_base_excel(request):
    file_path = PATH_template + 'list.xlsx'
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(),
                                    content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="UT模板.xlsx"'  # 设置下载文件的名称
            return response
    else:
        return HttpResponse('File not found.', status=404)

