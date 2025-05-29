from django.shortcuts import render

def index(request):
    return render(request, 'les_ex_1/index.html')


def page2(request):
    return render(request, 'les_ex_1/page2.html')


def page3(request):
    return render(request, 'les_ex_1/page3.html')


def page4(request):
    return render(request, 'les_ex_1/page4.html')
