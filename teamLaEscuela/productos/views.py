from django.shortcuts import redirect, render

from .carro import Carro #importamos la clase carro con metodos y funciones 
from .models import Juegos
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.db.models import Q


from productos.forms import juegosForm

from django.views.generic.detail import DetailView

from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required




def comprobante(request):
   return render(request,'productos/comprobante.html')
# Create your views here.
class listaJuegos(ListView): #poner como views por que usa listas 
    model=Juegos
    template_name= 'productos/homepag.html' #FIJA NO SE TOCA
    paginate_by= 4
    def get_queryset(self):
        query = self.request.GET.get('prd')
        categoria = self.request.GET.get('categoria')
        if categoria:
            object_list = self.model.objects.filter(Q(categoria__icontains=categoria))
            print("object_list: ",object_list)   
        elif query:
            object_list = self.model.objects.filter(Q(nombre__icontains=query)|
            Q(desarrolladora__icontains=query))
      
        else:
            object_list = self.model.objects.all()
            print("object_list else: ",object_list)
        return object_list


class HomePageView(ListView): #poner como views por que usa listas 
    model= Juegos
    template_name= 'productos/home.html' #FIJA NO SE TOCA 


class juegosListView(ListView):
    model=Juegos
    template_name= 'productos/juegos_list.html'
    paginate_by= 5
    def get_queryset(self):
        query = self.request.GET.get('prd')
        categoria = self.request.GET.get('categoria')
        if categoria:
            object_list = self.model.objects.filter(Q(categoria__icontains=categoria))
            print("object_list: ",object_list)   
        elif query:
            object_list = self.model.objects.filter(Q(nombre__icontains=query)|
            Q(desarrolladora__icontains=query))
      
        else:
            object_list = self.model.objects.all()
            print("object_list else: ",object_list)
        return object_list
    

class juegosCreate(CreateView):
    model=Juegos
    #fields = ['nombre', 'descripcion','categoria','desarrolladora','fecha_de_lanzamiento','precio', 'imagen']
    form_class= juegosForm
    template_name= 'productos/juegos_form.html'
    success_url = reverse_lazy('juegos')

#################################################################################


class juegosUpdate(UpdateView):
    model=Juegos
    #fields = ['nombre', 'descripcion','categoria','desarrolladora','fecha_de_lanzamiento','precio', 'imagen']
    form_class = juegosForm
    template_name= 'productos/juegos_update_form.html'
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse_lazy('juegos')+'?Actualizado'


class juegosDelete(DeleteView):
    model = Juegos
    #template_name= 'productos/juegos_confirm_delete.html'
    success_url = reverse_lazy('juegos')      
###################################################################################


class juegosDetailView(DetailView):
    model = Juegos
    form_class = juegosForm
    template_name_suffix = '_detail'





@login_required(login_url='/')
def tienda(request):
    juegos=Juegos.objects.all()
    return render(request,"productos/tienda.html",{juegos:'juegos'})

# Create your views here.
@login_required(login_url='/')
def agregar_juego(request,juego_id): #recibe como parametro la peticion y el parametro
    carro=Carro(request)
    juego=Juegos.objects.get(id=juego_id)#obtenemos el ide del producto
    carro.agregar(juego)
    return redirect('tienda')


def eliminar_juego(request,juego_id):
    carro=Carro(request)
    juego=Juegos.objects.get(id=juego_id)
    carro.borrar_juego(juego=juego)
    return redirect('tienda')

def restar_juego(request,juego_id):
    carro=Carro(request)
    juego=Juegos.objects.get(id=juego_id)
    carro.restar(juego)
    return redirect('tienda')

def vaciar_carro(request):
    carro=Carro(request)
    carro.vaciar_carro()
    return redirect('tienda')









