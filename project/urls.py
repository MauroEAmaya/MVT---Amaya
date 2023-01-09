"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from ejemplo.views import (index, saludar_a, sumar, 
                            monstrar_familiares, 
                            BuscarFamiliar, AltaFamiliar,
                            ActualizarFamiliar, BorrarFamiliar,
                            monstrar_mascotas,monstrar_actividades,
                            BuscarMascota, BuscarActividad,
                            AltaMascota, AltaActividad,
                            ActualizarMascota, ActualizarActividad,
                            BorrarMascota, BorrarActividad,
                            FamiliarList, FamiliarDetalle, FamiliarCrear,
                            FamiliarBorrar, FamiliarActualizar) 
from rol_y_aventura.views import (index, PostList, PostCrear, PostDetalle,
                                 PostBorrar, PostActualizar, UserSignUp, UserLogin,
                                 UserLogout,AvatarActualizar, UserActualizar,
                                 MensajeCrear, MensajeListar, MensajeDetalle,MensajeBorrar,about)
from django.contrib.admin.views.decorators import staff_member_required                                 

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('saludar/', index),
    #path("saludar-a/<nombre>/", saludar_a),
    #path("sumar/<int:a>/<int:b>", sumar),
    #path('mi-familia/', monstrar_familiares),
    #path('mi-mascota/', monstrar_mascotas),
    #path('mi-actividad/', monstrar_actividades),
    #path('mi-familia/buscar', BuscarFamiliar.as_view()),
    #path('mi-mascota/buscar', BuscarMascota.as_view()),
    #path('mi-actividad/buscar', BuscarActividad.as_view()),
    #path('mi-familia/alta', AltaFamiliar.as_view()),
    #path('mi-mascota/alta', AltaMascota.as_view()),
    #path('mi-actividad/alta', AltaActividad.as_view()),
    #path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()),
    #path('mi-mascota/actualizar/<int:pk>', ActualizarMascota.as_view()),
    #path('mi-actividad/actualizar/<int:pk>', ActualizarActividad.as_view()),
    #path('mi-familia/borrar/<int:pk>', BorrarFamiliar.as_view()),
    #path('mi-mascota/borrar/<int:pk>', BorrarMascota.as_view()),
    #path('mi-actividad/borrar/<int:pk>', BorrarActividad.as_view()),
    #path('panel-familia/<int:pk>/detalle', FamiliarDetalle.as_view()),
    #path('panel-familia/', FamiliarList.as_view()),
    #path('panel-familia/crear', FamiliarCrear.as_view()),
    #path('panel-familia/<int:pk>/borrar', FamiliarBorrar.as_view()),
    #path('panel-familia/<int:pk>/actualizar', FamiliarActualizar.as_view()),
    #path('success_updated_message/', TemplateView.as_view(template_name="ejemplo/success_updated_message.html")),
    #path('ejemplo-dos/', index, name="ejemplo-dos-index"),
    #path('ejemplo-dos/<int:pk>/detalle/', PostDetalle.as_view(), name="ejemplo-dos-detalle"),
    #path('ejemplo-dos/listar/', PostList.as_view(), name="ejemplo-dos-listar"),
    #path('ejemplo-dos/crear/', staff_member_required (PostCrear.as_view()), name="ejemplo-dos-crear"),
    #path('ejemplo-dos/<int:pk>/borrar/', staff_member_required (PostBorrar.as_view()), name="ejemplo-dos-borrar"),
    #path('ejemplo-dos/<int:pk>/actualizar/', staff_member_required (PostActualizar.as_view()), name="ejemplo-dos-actualizar"),
    #path("ejemplo-dos/signup/", UserSignUp.as_view(),name="ejemplo-dos-signup"),
    #path("ejemplo-dos/login/", UserLogin.as_view(),name="ejemplo-dos-login"),
    #path("ejemplo-dos/logout/", UserLogout.as_view(),name="ejemplo-dos-logout"),
    #path("ejemplo-dos/avatars/<int:pk>/actualizar/",AvatarActualizar.as_view(), name="ejemplo-dos-avatars-actualizar"),
    #path("ejemplo-dos/users/<int:pk>/actualizar/",UserActualizar.as_view(), name="ejemplo-dos-users-actualizar"),
    #path("ejemplo-dos/mensajes/crear/", MensajeCrear.as_view(), name="ejemplo-dos-mensajes-crear"),
    #path("ejemplo-dos/mensajes/<int:pk>/detalle/", MensajeDetalle.as_view(), name="ejemplo-dos-mensajes-detalle"),
    #path("ejemplo-dos/mensajes/listar/", MensajeListar.as_view(), name="ejemplo-dos-mensajes-listar"),
    path('rol_y_aventura/', index, name="rol-y-aventura-index"),
    path('rol_y_aventura/<int:pk>/detalle/', PostDetalle.as_view(), name="rol-y-aventura-detalle"),
    path('rol_y_aventura/listar/', PostList.as_view(), name="rol-y-aventura-listar"),
    path('rol_y_aventura/crear/', staff_member_required (PostCrear.as_view()), name="rol-y-aventura-crear"),
    path('rol_y_aventura/<int:pk>/borrar/', staff_member_required (PostBorrar.as_view()), name="rol-y-aventura-borrar"),
    path('rol_y_aventura/<int:pk>/actualizar/', staff_member_required (PostActualizar.as_view()), name="rol-y-aventura-actualizar"),
    path("rol_y_aventura/signup/", UserSignUp.as_view(),name="rol-y-aventura-signup"),
    path("rol_y_aventura/login/", UserLogin.as_view(),name="rol-y-aventura-login"),
    path("rol_y_aventura/logout/", UserLogout.as_view(),name="rol-y-aventura-logout"),
    path("rol_y_aventura/avatars/<int:pk>/actualizar/",AvatarActualizar.as_view(), name="rol-y-aventura-avatars-actualizar"),
    path("rol_y_aventura/users/<int:pk>/actualizar/",UserActualizar.as_view(), name="rol-y-aventura-users-actualizar"),
    path("rol_y_aventura/mensajes/crear/", MensajeCrear.as_view(), name="rol-y-aventura-mensajes-crear"),
    path("rol_y_aventura/mensajes/<int:pk>/detalle/", MensajeDetalle.as_view(), name="rol-y-aventura-mensajes-detalle"),
    path("rol_y_aventura/mensajes/listar/", MensajeListar.as_view(), name="rol-y-aventura-mensajes-listar"),
    path("rol_y_aventura/mensajes/<int:pk>/borrar/", MensajeBorrar.as_view(), name="rol-y-aventura-mensajes-borrar"),
    path('rol_y_aventura/about/', about, name="rol-y-aventura-about"),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

