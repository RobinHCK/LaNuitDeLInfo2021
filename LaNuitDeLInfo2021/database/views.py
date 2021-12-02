from django.shortcuts import render


def drop(request):
    return render(request, 'database/drop.html')

def search(request):
    return render(request, 'database/search.html')
