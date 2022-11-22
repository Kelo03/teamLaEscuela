from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.conf import settings

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LoginView #LoginView importado para el login de los usuarios


# Create your views here.

def contacto(request):
   if request.method=="POST":
        #subject=request.POST["asunto"]
        textUser=  "\nNOMBRE y APELLIDO: " + request.POST["nombre"] + " " + request.POST["apellido"] + "\nCORREO ELECTRONICO: " + request.POST["email"] +  "\nNº TELEFONO: " + request.POST["telefono"] + "\nMENSAJE: " + request.POST["mensaje"]
        email_form=settings.EMAIL_HOST_USER
        recipient_list=["ezequiel_30_12@hotmail.com"]
        send_mail(request.POST["asunto"], textUser, email_form, recipient_list)
        
        textUser="Su mensaje se ha enviado correctamente, le respondemos a la brevedad!"
        recipient_list=[request.POST["email"]]
        send_mail(request.POST["asunto"], textUser, email_form, recipient_list)

        mensaje="Su correo se ha enviado correctamente"
        return render(request,"core/contacto.html" ,{"mensaje":mensaje})
   return render(request,'core/contacto.html')

def acercade(request):
   return render(request,'core/acercade.html')

#@login_required(login_url='/')
def faqs(request):
   return render(request,'core/faqs.html')

def nuevo(request):
   return render(request,'core/nuevo.html')


class LoginFormView(LoginView):
   template_name= "core/login.html"
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['title'] = 'Iniciar sesion'
      return context


def signup(request):
    if request.method == 'GET':
        return render(request, 'core/signup.html', {"form": UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('principal')
            except IntegrityError:
                return render(request, 'core/signup.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'core/signup.html', {"form": UserCreationForm, "error": "Passwords did not match."})




def signout(request):
    logout(request)
    return redirect('principal')

