from django.shortcuts import render


def chrome(request):
    context = {'message':'Django 很棒'}
    return render(request, 'chrome/chrome.html', context)