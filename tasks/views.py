from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.mail import send_mail
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def create_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        due_date = request.POST['due_date']
        is_completed = False
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        Task.objects.create(title=title, description=description, due_date=due_date, is_completed=is_completed,
                            email=email, phone_number=phone_number)
        return redirect('task_list')
    return render(request, 'tasks/create_task.html')


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.due_date = request.POST['due_date']
        task.email = request.POST['email']
        task.phone_number = request.POST['phone_number']
        task.save()
        return redirect('task_list')

    return render(request, 'tasks/edit_task.html', {'task': task})


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')


def mark_task_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = True
    task.save()
    return redirect('task_list')


def mark_task_incomplete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = False
    task.save()
    return redirect('task_list')


def send_email(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        recipient_list = [task.email]
        subject = f"Task: {task.title}"
        message = task.description
        send_mail(subject, message, 'your_email@example.com', recipient_list)
        return redirect('task_list')

    return render(request, 'tasks/send_email.html', {'task': task})


def make_phone_call(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        # Perform phone call action using a phone call API or library
        return redirect('task_list')

    return render(request, 'tasks/make_phone_call.html', {'task': task})