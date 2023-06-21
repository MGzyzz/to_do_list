from django.shortcuts import render, redirect
from .models import Task
# Create your views here.


def views_all(request):
    return render(
        request, 'home.html', context={
            'tasks': Task.objects.order_by('description')
        }
    )


def new_task(request):
    if request.method == 'POST':
        data = request.POST
        task_data = {
            'name': data.get('name'),
            'description': data.get("description"),
            'status': data.get("status"),
            'start_date': data.get('start_date'),
            'date_of_completion': data.get("completion_date")
        }
        task = Task.objects.create(**task_data)
        return redirect('task-detail', id=task.id)
    else:
        context = {'status_choices': Task.TASK_STATUS_CHOICE}
        return render(request, 'task_create.html', context)


def task_detail_view(request, id: int):
    task = Task.objects.get(id=id)
    return render(request, 'task_detail.html', context={'task': task})