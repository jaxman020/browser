from django.shortcuts import render


def sarafi(request):
    context = {'message':'Django 很棒'}
    return render(request, 'sarafi/sarafi.html', context)