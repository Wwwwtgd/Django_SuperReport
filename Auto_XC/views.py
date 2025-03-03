from django.shortcuts import render


# Create your views here.
def ut(request):
    return render(request, 'ut.html')


def mt(request):
    return render(request, 'mt.html')
