from django.shortcuts import render, redirect
from app.models import Task
from django.http import HttpResponse
from django.views import generic, View
from app.forms import TaskForm, TaskUpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.


def My_Task(request):
    upcoming_tasks= Task.objects.filter(user=request.user, complete=False)
    complete_tasks= Task.objects.filter(user=request.user, complete=True)
    return render(request,'app/Tasks.html',context={'U_tasks':upcoming_tasks,'C_tasks':complete_tasks})

def home(request):
    return render(request,'app/Home.html')

class TaskCreateView(LoginRequiredMixin,generic.CreateView):
    login_url = reverse_lazy('login')
    model = Task
    form_class = TaskForm
    template_name = "app/Task Create.html"
    success_url = reverse_lazy('My Task')

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskDetailView(LoginRequiredMixin,generic.DetailView):
    model = Task
    template_name = "app/Task Details.html"
    login_url=reverse_lazy('login')

class TaskUpdateView(LoginRequiredMixin,UserPassesTestMixin,generic.UpdateView):
    login_url=reverse_lazy('login')
    model = Task
    form_class = TaskUpdateForm
    template_name = 'app/Task Update.html'
    success_url = reverse_lazy('My Task')

    def form_valid(self,form):
        form.instance.user = self.request.user
        form.instance.complete = False
        return super().form_valid(form)
    
    def test_func(self, *args, **kwargs):
        task= Task.objects.get(id=self.kwargs.get('pk'))
        if task.user== self.request.user:
            return True
        else:
            return False

class TaskDeleteView(LoginRequiredMixin,UserPassesTestMixin,generic.DeleteView):
    login_url=reverse_lazy("login")
    model = Task
    template_name = "app/Task Delete.html"
    success_url = reverse_lazy('My Task')

    def test_func(self, *args, **kwargs):
        task= Task.objects.get(id=self.kwargs.get('pk'))
        if task.user== self.request.user:
            return True
        else:
            return False

class TaskCompleteView(View):
    def get(self,request,id):
        task= Task.objects.get(id=id)
        if task.complete==False:
            task.complete=True
            task.save()
            return redirect(reverse_lazy('My Task'))
        else:
            return HttpResponse('Task Was Already Completed')