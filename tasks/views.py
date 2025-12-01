from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Task
from django.db.models import Q 


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # After registration, go to login page
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'tasks/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('task_list')
    else:
        form = AuthenticationForm()
    return render(request, 'tasks/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def task_list(request):
    # Read filters from URL query parameters
    q = request.GET.get('q', '').strip()              # search text
    status = request.GET.get('status', 'ALL')         # TODO / IN_PROGRESS / DONE / ALL
    priority = request.GET.get('priority', 'ALL')     # HIGH / MEDIUM / LOW / ALL

    tasks = Task.objects.filter(user=request.user)

    # Apply search filter if there's a query
    if q:
        tasks = tasks.filter(
            Q(title__icontains=q) | Q(description__icontains=q)
        )

    # Apply status filter
    if status != 'ALL':
        tasks = tasks.filter(status=status)

    # Apply priority filter
    if priority != 'ALL':
        tasks = tasks.filter(priority=priority)

        tasks = tasks.order_by('status', 'due_date')

    # Stats based on the filtered tasks
    total_tasks = tasks.count()
    done_tasks = tasks.filter(status='DONE').count()
    todo_tasks = tasks.filter(status='TODO').count()
    in_progress_tasks = tasks.filter(status='IN_PROGRESS').count()

    high_priority = tasks.filter(priority='HIGH').count()
    medium_priority = tasks.filter(priority='MEDIUM').count()
    low_priority = tasks.filter(priority='LOW').count()

    context = {
        'tasks': tasks,
        'q': q,
        'current_status': status,
        'current_priority': priority,
        'total_tasks': total_tasks,
        'done_tasks': done_tasks,
        'todo_tasks': todo_tasks,
        'in_progress_tasks': in_progress_tasks,
        'high_priority': high_priority,
        'medium_priority': medium_priority,
        'low_priority': low_priority,
    }
    return render(request, 'tasks/task_list.html', context)




@login_required
def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        status = request.POST.get('status', 'TODO')
        priority = request.POST.get('priority', 'MEDIUM')
        due_date = request.POST.get('due_date') or None

        Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            status=status,
            priority=priority,
            due_date=due_date,
        )
        return redirect('task_list')

    return render(request, 'tasks/task_form.html')


@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description', '')
        task.status = request.POST.get('status', 'TODO')
        task.priority = request.POST.get('priority', 'MEDIUM')
        task.due_date = request.POST.get('due_date') or None
        task.save()
        return redirect('task_list')

    return render(request, 'tasks/task_form.html', {'task': task})


@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'POST':
        task.delete()
        return redirect('task_list')

    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
