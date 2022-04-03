from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
# Create your views here.


def index(request):
    tasks = Task.objects.all() # данные из task в шаблон
    #tasks = Task.objects.order_by('title')  # данные из task в шаблон сортированные по полю  title или иные
    return render(request, 'main/index.html', {'title': 'Главная страница сайта',
                                               'tasks': tasks}) # какой шаблон будем подргружать и что передавать в шаблон
    # return HttpResponse("<h4>Hello</h4>") # выводим текст вместо httpresponse обычно используют render


def about(request):
    return render(request, 'main/about.html')
    #return HttpResponse("<h4>about</h4>") # выводим текст

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'


    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)

