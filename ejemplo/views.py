from django.shortcuts import render, get_object_or_404
from ejemplo.models import Familiar, Mascota, Actividad
from ejemplo.forms import Buscar, FamiliarForm, MascotaForm, ActividadForm
from django.views import View 
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView   

def index(request):
    return render(request, "ejemplo/saludar.html")

def saludar_a(request, nombre):
    
    return render(request,
    "ejemplo/saludar_a.html",
    {"nombre": nombre}
    ) 

def sumar(request, a, b):
    return render (request, 
    "ejemplo/sumar.html",
    {"a": a,
    "b": b,
    "resultado": a + b
    }
    )

def monstrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, 
  "ejemplo/familiares.html", 
  {"lista_familiares": lista_familiares}                                                                                                                                                                                                                                        
  )

def monstrar_mascotas(request):
  lista_mascotas = Mascota.objects.all()
  return render(request, 
  "ejemplo/mascotas.html", 
  {"lista_mascotas": lista_mascotas}                                                                                                                                                                                                                                        
  )

def monstrar_actividades(request):
    lista_actividades = Actividad.objects.all()
    return render(request, 
    "ejemplo/actividades.html", 
    {"lista_actividades": lista_actividades}                                                                                                                                                                                                                                        
    )

class BuscarFamiliar(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})

class BuscarMascota(View):
    form_class = Buscar
    template_name = 'ejemplo/buscaractividad.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_mascotas = Mascota.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_mascotas':lista_mascotas})
        return render(request, self.template_name, {"form": form})     

class BuscarActividad(View):
    form_class = Buscar
    template_name = 'ejemplo/buscaractividad.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_actividades = Actividad.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_actividades':lista_actividades})
        return render(request, self.template_name, {"form": form})           

class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "nacimiento":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class AltaMascota(View):

    form_class = MascotaForm
    template_name = 'ejemplo/alta_mascota.html'
    initial = {"nombre":"", "raza":"", "edad":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito la mascota {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})


class AltaActividad(View):

    form_class = ActividadForm
    template_name = 'ejemplo/alta_actividad.html'
    initial = {"nombre":"", "dia":"", "horario":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito la actividad {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})



class ActualizarFamiliar(View):
  form_class = FamiliarForm
  template_name = 'ejemplo/actualizar_familiar.html'
  initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}
  
  
  def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(instance=familiar)
      return render(request, self.template_name, {'form':form,'familiar': familiar})

  
  def post(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(request.POST ,instance=familiar)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito el familiar {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'familiar': familiar,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})

class ActualizarMascota(View):
  form_class = MascotaForm
  template_name = 'ejemplo/actualizar_mascota.html'
  initial = {"nombre":"", "raza":"", "edad":""}
  
  
  def get(self, request, pk): 
      mascota = get_object_or_404(Mascota, pk=pk)
      form = self.form_class(instance=mascota)
      return render(request, self.template_name, {'form':form,'mascota': mascota})

  
  def post(self, request, pk): 
      mascota = get_object_or_404(Mascota, pk=pk)
      form = self.form_class(request.POST ,instance=mascota)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito la mascota {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'mascota': mascota,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})


class ActualizarActividad(View):
  form_class = ActividadForm
  template_name = 'ejemplo/actualizar_actividad.html'
  initial = {"nombre":"", "dia":"", "horario":""}
  
  
  def get(self, request, pk): 
      actividad = get_object_or_404(Actividad, pk=pk)
      form = self.form_class(instance=actividad)
      return render(request, self.template_name, {'form':form,'actividad': actividad})

  
  def post(self, request, pk): 
      actividad = get_object_or_404(Actividad, pk=pk)
      form = self.form_class(request.POST ,instance=actividad)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito la actividad {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'actividad': actividad,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})            

class BorrarFamiliar(View):
  template_name = 'ejemplo/familiares.html'
  
  def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      familiar.delete()
      familiar = Familiar.objects.all()
      return render(request, self.template_name, {'lista_familiares': familiar})

class BorrarMascota(View):
  template_name = 'ejemplo/mascotas.html'
  
  def get(self, request, pk): 
      mascota = get_object_or_404(Mascota, pk=pk)
      mascota.delete()
      mascota = Mascota.objects.all()
      return render(request, self.template_name, {'lista_mascotas': mascota})   


class BorrarActividad(View):
  template_name = 'ejemplo/actividades.html'
  
  def get(self, request, pk): 
      actividad = get_object_or_404(Actividad, pk=pk)
      actividad.delete()
      actividad = Actividad.objects.all()
      return render(request, self.template_name, {'lista_actividades': actividad})  

class FamiliarList(ListView):
  model = Familiar  

class FamiliarDetalle (DetailView):
  model = Familiar

class FamiliarCrear(CreateView):
  model = Familiar
  success_url = "/panel-familia"
  fields = ["nombre", "direccion", "nacimiento"]

class FamiliarBorrar(DeleteView):
  model = Familiar
  success_url = "/panel-familia"

class FamiliarActualizar(UpdateView):
  model = Familiar
  success_url = "/success_updated_message"
  fields = ["nombre", "direccion", "nacimiento"]