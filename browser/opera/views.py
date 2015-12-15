from django.shortcuts import render

# Create your views here.
def opera(request):
    context = {'message':'Django 很棒'}
    return render(request, 'opera/opera.html', context)