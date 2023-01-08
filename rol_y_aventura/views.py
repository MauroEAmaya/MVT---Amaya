from django.shortcuts import render
from django.views.generic import ListView , CreateView, DeleteView, UpdateView, DetailView
from rol_y_aventura.models import  Post   
from django.urls import reverse_lazy 
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from rol_y_aventura.forms import UsuarioForm
from rol_y_aventura.models import Avatar, Post, Mensaje
from django.contrib.auth.models import User

#@login_required
def index(request):
    posts = Post.objects.order_by("-publicado_el").all()
    return render(request,"rol_y_aventura/index.html", {"posts": posts})

class PostDetalle(LoginRequiredMixin, DetailView):
    model = Post

class PostList(LoginRequiredMixin, ListView):
    model = Post
    
   
class PostCrear(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy("rol-y-aventura-listar")
    fields = "__all__"

class PostBorrar(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("rol-y-aventura-listar")
    fields = "__all__"


class PostActualizar(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("rol-y-aventura-listar")
    fields = "__all__"

class UserSignUp(CreateView):
    form_class=UsuarioForm
    template_name= "registration/signup.html"
    success_url=reverse_lazy("rol-y-aventura-listar")   

class UserLogin(LoginView):
    next_page= reverse_lazy("rol-y-aventura-listar")  

class UserLogout(LogoutView):
    next_page= reverse_lazy("rol-y-aventura-listar")    

class MensajeDetalle(LoginRequiredMixin, DetailView):
    model = Mensaje

class MensajeListar(LoginRequiredMixin, ListView):
    model = Mensaje  

class MensajeCrear(CreateView):
    model = Mensaje
    success_url = reverse_lazy("rol-y-aventura-mensajes-crear")
    fields = ['nombre', 'email', 'texto']
    success_message = "Mensaje de contacto enviado!!"

class MensajeBorrar(DeleteView):
    model = Mensaje
    success_url = reverse_lazy("rol-y-aventura-mensajes-listar")

class AvatarActualizar (UpdateView):
    model= Avatar
    fields=["imagen"]
    success_url= reverse_lazy("rol-y-aventura-listar")

class UserActualizar(UpdateView):
    model = User
    fields = ["first_name","last_name","email"]
    success_url= reverse_lazy("rol-y-aventura-listar")
