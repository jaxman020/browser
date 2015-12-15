from django.shortcuts import render


def firefox(request):
    context = {'message':'Django 很棒'}
    return render(request, 'firefox/firefox.html', context)