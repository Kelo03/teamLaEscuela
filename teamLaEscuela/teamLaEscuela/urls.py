"""teamLaEscuela URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from core import views
from django.conf import settings
from productos import views as productos_views
from core.views import LoginFormView
from productos.views import *

urlpatterns = [
    path('', LoginFormView.as_view()),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),

    path('home/',productos_views.HomePageView.as_view(), name='principal'),
    path('acercade/', views.acercade),
    path('contacto/', views.contacto),
    path('faqs/', views.faqs),
    path('comprobante/', productos_views.comprobante),
    path('juegos/', productos_views.juegosListView.as_view(), name='juegos'),
    #path('juegosCategorias/', productos_views.juegosCategorias),

    
    path('create/', productos_views.juegosCreate.as_view(), name='create'),
    path('update/<int:pk>/', productos_views.juegosUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', productos_views.juegosDelete.as_view(), name='delete'),
    path('detail/<int:pk>/', productos_views.juegosDetailView.as_view(), name='detail'),


    path('tienda/',productos_views.tienda,name="tienda"),
    path('agregar/<int:juego_id>/',productos_views.agregar_juego, name='agregar'),
    path('eliminar/<int:juego_id>/',productos_views.eliminar_juego, name='eliminar'),
    path('restar/<int:juego_id>/',productos_views.restar_juego, name='sub'),
    path('limpiar/',productos_views.vaciar_carro, name='CLS'),

    path('nuevo/', views.nuevo),
    path('admin/', admin.site.urls),
    
    #path('buscar/', productos_views.buscar),

]






#Configuración extendida para mostrar las imágenes en modo debug
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
