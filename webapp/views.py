from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def construction(request):
    return render(request, 'construction_page.html')
