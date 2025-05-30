from django.shortcuts import render

def home(request):
    return render(request, 'les_ex_1/news.html')