from django.db import models

# Create your models here.

class Juegos(models.Model):
    nombre=models.CharField(max_length=200, verbose_name="Nombre")
    descripcion=models.TextField(verbose_name="Descripcion") 
    categoria=models.TextField(verbose_name="Categoria")
    desarrolladora=models.TextField(verbose_name="Desarrolladora") 
    fecha_de_lanzamiento=models.TextField(verbose_name="Lanzamiento") 
    precio=models.FloatField(verbose_name="Precio")
    

    imagenSmall=models.ImageField(verbose_name="Imagen", upload_to = "juegos")
    imagenBig=models.ImageField(verbose_name="Imagen2",upload_to = "juegos" )
    created=models.DateTimeField(auto_now_add=True)

    updated=models.DateTimeField(auto_now=True)



    class Meta:
        verbose_name="juego"
        verbose_name_plural= "juegos"
        ordering = ["-created"] #ORDEN DESCENDENTE 

    def __str__(self):
        return self.nombre