import os
import zipfile
from io import BytesIO
import docx
from django.http import JsonResponse, HttpResponse
path_all = 'Auto_LH/GB_Script/report/'


def get_form_data(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        # 处理表单数据
        return HttpResponse(f'接收到的用户名：{username}')


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