from django.shortcuts import render
from .models import Todo

def index(request):
    todos = Todo.objects.all().order_by('-pk')

    
    return render(
		request,
		'todo_app/index.html',
		{
			'todos' : todos,
		}
	)
# Create your views here.
