import os
import zipfile
from io import BytesIO
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse, HttpResponse
from django.core.files.storage import FileSystemStorage
from .script.autoEdit_MT import auto_edit_mt
PATH_template = os.getcwd() + r'/Auto_XC/MT_Script/report_template/'
PATH_result = os.getcwd() + r'/Auto_XC/MT_Script/report_result/'
result_path = PATH_result


def download_mt_base_excel(request):
    file_path = PATH_template + 'A_MT模板.xlsx'
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(),
                                    content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="MT_list.xlsx"'  # 设置下载文件的名称
            return response
    else:
        return HttpResponse('File not found.', status=404)


def download_mt_report(request):
    # 设置文件夹路径
    folder_path = result_path
    zip_buffer = BytesIO()
    # 创建一个 Zip 文件
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for folder_name, sub_folders, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(folder_name, filename)
                zip_file.write(file_path, os.path.relpath(file_path, folder_path))
    # 设置响应头，告知浏览器是文件下载
    zip_buffer.seek(0)
    response = HttpResponse(zip_buffer.read(), content_type='application/zip')
    response['Content-Disposition'] = 'attachment;'
    return response


@csrf_protect  # 确保启用 CSRF 防护
def get_mt_list(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage(location=PATH_template)
        # 如果文件已经存在，删除旧文件  原文件名：PATH_template + uploaded_file.name
        if os.path.exists(PATH_template + "mt_now.xlsx"):
            os.remove(PATH_template + "mt_now.xlsx")
        filename = fs.save("mt_now.xlsx", uploaded_file)
        fs.url(filename)  # 返回文件的 URL
        excel_path = os.path.join(PATH_template, filename)
        global result_path
        result_path = auto_edit_mt(excel_path)  # 调用自动化脚本进行处理
        return JsonResponse({'status': 'success', 'msg': '生成报告成功'})
    return JsonResponse({'status': 'error', 'msg': '上传/生成报告失败'}, status=400)


@csrf_protect  # 确保启用 CSRF 防护
def update_mt_picture(request):
    if request.method == 'POST' and request.FILES.get('file'):
        # 获取上传的文件
        file = request.FILES['file']
        fs = FileSystemStorage(location=PATH_template)
        # 如果文件已经存在，删除旧文件
        if os.path.exists(PATH_template + '示意图.png'):
            os.remove(PATH_template + '示意图.png')
        filename = fs.save('示意图.png', file)
        fs = FileSystemStorage()
        # 获取文件的 URL
        file_url = fs.url(filename)
        # 你可以选择返回文件的 URL 或其他信息
        return JsonResponse({
            'code': 0,  # 0 表示上传成功
            'msg': '上传成功',
            'data': {
                'src': file_url  # 返回文件的 URL
            }
        })
    return JsonResponse({'code': 1, 'msg': '上传失败'})
