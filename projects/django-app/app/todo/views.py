from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem

def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(
        request=request,
        template_name="todo.html",
        context={'all_items': all_todo_items}
    )

def addTodo(request):
    item = request.POST['content']
    new_todo_item = TodoItem(content=item)
    new_todo_item.save()
    return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):
    item = TodoItem.objects.get(id=todo_id)
    item.delete()
    return HttpResponseRedirect('/todo/')
