from django import forms
from ejemplo.models import Familiar
from ejemplo.models import Mascota
from ejemplo.models import Actividad

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100,
                            widget=forms.TextInput(attrs={"placeholder": "ingrese nombre..."}))    
    
class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'nacimiento']

class MascotaForm(forms.ModelForm):
  class Meta:
    model = Mascota
    fields = ['nombre', 'raza', 'edad']    

class ActividadForm(forms.ModelForm):
  class Meta:
    model = Actividad
    fields = ['nombre', 'dia', 'horario'] 