from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST
from .models import Todolist
from .forms import TodoForms

def index(request):
    todo_list = Todolist.objects.order_by('id')

    form =TodoForms()

    context = {'todo_list' : todo_list, 'form' : form}

    return render(request,'index.html',context)
@require_POST
def addTodo(request):
    form = TodoForms(request.POST)

    if form.is_valid():
        new_todo = Todolist(text=request.POST['text'])
        new_todo.save()
        return redirect('index')
def completeTodo(request,todo_id):
    todo = Todolist.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    return redirect('index')

def deletecompleted(request):
    Todoobj = Todolist.objects.filter(complete__exact = True)
    Todoobj.delete()
    return redirect('index')
def delall(request):
    Todolist.objects.all().delete()

    return redirect('index')

