from django.shortcuts import render


def explorer(request):
    context = {'message':'Django 很棒'}
    return render(request, 'explorer/explorer.html', context)