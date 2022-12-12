from django.shortcuts import render


def home(request):
    name = 'Anton'
    return render(request, 'home.html', {'name': name})


def about(request):
    name = 'About'
    return render(request, 'about.html', {'name': name})
