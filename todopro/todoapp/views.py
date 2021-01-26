from django.shortcuts import render, redirect

from .models import Task
from .forms import ToDoforms
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = 'task_view.html'
    context_object_name = 'p'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'i'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'edit.html'
    context_object_name = 'task'
    fields = ('Name', 'Priority', 'Date')

    def get_success_url(self):
        return reverse_lazy('cvdetail', kwargs={'pk': self.object.id})


class TaskDeletelView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cvtask')


def task_view(request):
    p = Task.objects.all()
    if request.method == 'POST':
        Name = request.POST.get('Name')
        Priority = request.POST.get('Priority')
        Date = request.POST.get('Date')
        t = Task(Name=Name, Priority=Priority, Date=Date)
        t.save()
    return render(request, 'task_view.html', {'p': p})


def delete(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html', {'task': task})


def update(request, id):
    task = Task.objects.get(id=id)
    form = ToDoforms(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'task': task, 'form': form})

# Create your views here.
