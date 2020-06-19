from django.shortcuts import render
from .models import Todo
from django.http import HttpResponseRedirect


def home(request):
    items = Todo.objects.all().order_by('-added_date')
    context = {
        'items': items
    }
    return render(request, 'main/index.html', context)


def add_todo(request):
    item = request.POST.get('to_do')
    Todo.objects.create(text=item)
    return HttpResponseRedirect('/')


def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')
