from django.shortcuts import render

def index(request):
    return render(request, 'les_ex_1/index.html')


def page2(request):
    return render(request, 'les_ex_1/page2.html')