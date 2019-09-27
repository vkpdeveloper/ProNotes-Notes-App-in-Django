from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Work
from datetime import date
import time

def index(request):
    newwork = request.POST.get('work')
    if request.method == 'POST':
        work = Work(work=newwork)
        work.save()
        data = Work.objects.all()
        n = len(data)
        parmas = {'range': n, 'data': data}
        return render(request, r'pronotes\index.html', parmas)
    else:
        data = Work.objects.all()
        n = len(data)
        parmas = {'range': n, 'data': data}
        return render(request, r'pronotes\index.html', parmas)

def delete(request):
    if request.method == 'GET':
        work = request.GET.get('work')
        print(work)
        parmas = {'work' : work}
        instance = Work.objects.get(work=work)
        instance.delete()
        return render(request, r'pronotes\delete.html', parmas)
