from django.shortcuts import render
from .models import Todo

def Todos(request):
    todos = Todo.objects.all().order_by('-pk')

    return render(
		request,
		'todo_app/todos.html',
		{
			'todos' : todos,
		}
	)
# Create your views here.
