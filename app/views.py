from datetime import date

from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ScheduleForm, TaskForm
from .models import Schedule, Task


def dashboard(request):
    today = date.today()
    today_name = today.strftime('%A')

    today_schedules = Schedule.objects.filter(day=today_name)
    upcoming_tasks = Task.objects.filter(deadline__gte=today).order_by('deadline')[:5]

    context = {
        'today_schedules': today_schedules,
        'upcoming_tasks': upcoming_tasks,
    }
    return render(request, 'dashboard.html', context)


def schedule_list(request):
    schedules = Schedule.objects.all()
    return render(request, 'schedules/schedule_list.html', {'schedules': schedules})


def schedule_add(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Schedule added successfully.')
            return redirect('app:schedule_list')
    else:
        form = ScheduleForm()

    return render(request, 'schedules/schedule_form.html', {'form': form})


def schedule_edit(request, pk):
    schedule = Schedule.objects.get(pk=pk)

    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            messages.success(request, 'Schedule updated successfully.')
            return redirect('app:schedule_list')
    else:
        form = ScheduleForm(instance=schedule)

    return render(request, 'schedules/schedule_form.html', {'form': form})


def schedule_delete(request, pk):
    schedule = Schedule.objects.get(pk=pk)

    if request.method == 'POST':
        schedule.delete()
        messages.success(request, 'Schedule deleted successfully.')
        return redirect('app:schedule_list')

    return render(request, 'schedules/schedule_confirm_delete.html', {'object': schedule})


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def task_add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task added successfully.')
            return redirect('app:task_list')
    else:
        form = TaskForm()

    return render(request, 'tasks/task_form.html', {'form': form})


def task_edit(request, pk):
    task = Task.objects.get(pk=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully.')
            return redirect('app:task_list')
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/task_form.html', {'form': form})


def task_delete(request, pk):
    task = Task.objects.get(pk=pk)

    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully.')
        return redirect('app:task_list')

    return render(request, 'tasks/task_confirm_delete.html', {'object': task})
