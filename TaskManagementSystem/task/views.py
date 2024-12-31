from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
from category.models import TaskCategory

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            categories = request.POST.getlist('categories')
            task.categories.set(categories)
            task.save()
            return redirect('show_tasks')
    else:
        form = TaskForm()
        categories = TaskCategory.objects.all()
    return render(request, 'task/add_task.html', {'form': form, 'categories': categories})


def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            categories = request.POST.getlist('categories')
            task.categories.set(categories)
            task.save()
            return redirect('show_tasks')
    else:
        form = TaskForm(instance=task)
        categories = TaskCategory.objects.all()
    return render(request, 'task/edit_task.html', {'form': form, 'categories': categories, 'task': task})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('show_tasks')
    return render(request, 'task/delete_task.html', {'task': task})

def show_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'task/show_tasks.html', {'tasks': tasks})


from django.shortcuts import redirect

def home(request):
    return redirect('show_tasks')