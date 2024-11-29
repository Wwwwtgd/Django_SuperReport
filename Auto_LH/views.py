from django.shortcuts import render


# Create your views here.
def gb(request):
    return render(request, 'gb.html')


def hc(request):
    return render(request, 'hc.html')


def hp(request):
    return render(request, 'hp.html')


def cs(request):
    return render(request, 'cs.html')