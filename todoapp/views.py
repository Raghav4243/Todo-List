from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from . import models
from django.urls import reverse_lazy,reverse
from django.http import HttpResponse,HttpResponseRedirect
from todoapp.forms import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as dj_login
from django.contrib.auth import logout as dj_logout

# Create your views here.


class TodoListView(ListView):
    model = models.Todo


class TodoCreateView(CreateView):
    fields = ('work',)
    model = models.Todo

class TodoDeleteView(DeleteView):
    model = models.Todo
    success_url = reverse_lazy('ListView')


class TododUpdateView(UpdateView):
    fields = ('work',)
    model = models.Todo

def register(request):
    u_form = UserForm()
    if request.method == 'POST':
        u_form = UserForm(request.POST)

        if u_form.is_valid():
            user = u_form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect(reverse('ListView'))
    else:
        print('error')
    return render(request,'todoapp/register.html',{'form':u_form})



def user_login(request):
    if request.method == 'POST':
        un = request.POST.get('user')
        ps = request.POST.get('pass')
        user = authenticate(username=un,password=ps)
        if user:
            if user.is_active:
                dj_login(request,user)
                return HttpResponseRedirect(reverse('ListView'))
            else:
                return HttpResponse("Account invalid")
        else:
            return render(request,'todoapp/todo_list.html')
    else:
        return render(request,'todoapp/login.html')


@login_required
def user_logout(request):
    dj_logout(request)
    return HttpResponseRedirect(reverse('ListView'))
