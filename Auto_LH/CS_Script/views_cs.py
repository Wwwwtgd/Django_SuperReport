import os
import zipfile
from io import BytesIO
import docx
from django.http import JsonResponse, HttpResponse


def download_base_excel(request):
    file_name = 'list.xlsx'
    file_path = 'Auto_LH/GB_Script/report/' + file_name
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{file_path.split("/")[-1]}"'
        return response


def download_docx_files(request):
    folder_path = 'Auto_LH/GB_Script/report/'
    zip_filename = "docx_files.zip"
    s = BytesIO()
    zf = zipfile.ZipFile(s, "w")
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith('.docx'):
                file_path = os.path.join(root, filename)
                zf.write(file_path, filename)
    zf.close()
    response = HttpResponse(s.getvalue(), content_type='application/zip')
    response['Content-Disposition'] = f'attachment; filename="{zip_filename}"'
    return response