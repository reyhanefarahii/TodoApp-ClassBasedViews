from django.shortcuts import redirect, render
from django.views.generic import ListView,UpdateView,DeleteView,CreateView
from .models import Task

# Create your views here.
class TaskView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = Task.objects.all()
        status = self.request.GET.get('status')

        if status == 'completed':
            queryset = queryset.filter(status=True)
        elif status == 'active':
            queryset = queryset.filter(status=False)

        return queryset

class TaskUpdate(UpdateView):
    model = Task
    fields = ['title']
    template_name = 'tasks/task_form.html'
    success_url = "/"

class TaskDelete(DeleteView):
    model = Task
    success_url = "/"
    # template_name = "geeks/geeksmodel_confirm_delete.html"

class TaskCreate(CreateView):
    model = Task
    fields = ['title']
    success_url = '/'


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        return redirect('task-list')

class TaskStatus(UpdateView):
    model = Task
    fields = ['status']
    success_url = '/'

    def post(self, request, *args, **kwargs):
        task = self.get_object()
        task.status = not task.status
        task.save()
        return redirect('task-list')