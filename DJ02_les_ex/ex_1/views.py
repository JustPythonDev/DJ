from django.shortcuts import render

def index(request):
    return render(request, 'ex_1/index.html')


def new(request):
    return render(request, 'ex_1/new.html')