from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Zuhdy Nadhif Ayyasy',
        'class': 'PBP C',
    }
    return render(request, 'main.html', context)