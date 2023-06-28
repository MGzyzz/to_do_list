from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Status
from To_do_list.forms import TaskForms
# Create your views here.


def views_all(request):
    if request.method == 'POST':
        selected_tasks = request.POST.getlist('task')
        for i in selected_tasks:
            Task.objects.filter(id=i).delete()
        return redirect('home')
    else:
        return render(
            request, 'home.html', context={
                'tasks': Task.objects.order_by('description')
            }
    )


def new_task(request):
    if request.method == 'POST':
        form = TaskForms(request.POST)
        if form.is_valid():
            task = Task.objects.create(
                name=request.POST.get('name'),
                description=request.POST.get('description'),
                status_id=request.POST.get('status'),
                start_date=request.POST.get('start_date'),
                date_of_completion=request.POST.get('date_of_completion')
            )
            return redirect('task-detail', id=task.id)
    else:
        form = TaskForms()
    return render(request, 'task_create.html', {'form': form, 'status': Status.objects.all()})


def task_detail_view(request, id: int):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('home')

    return render(request, 'task_detail.html', context={'task': task})


def task_edit(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'GET':
        form = TaskForms(initial={
            'name': task.name,
            'description': task.description,
            'status': task.status
        })
        return render(request, 'task_edit.html', {'task': task, 'status': Status.objects.all(), 'form': form})
    elif request.method == 'POST':
        form = TaskForms(data=request.POST)
        print(form)
        if form.is_valid():
            task.name = request.POST.get('name')
            task.description = request.POST.get('description')
            task.status_id = request.POST.get('status')
            task.save()
            return redirect('task-detail', id=task.id)
        else:
            return render(request, 'task_edit.html', {'task': task, 'status': Status.objects.all(), 'form': form})