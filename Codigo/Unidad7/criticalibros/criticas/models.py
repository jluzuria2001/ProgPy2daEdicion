from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=70,help_text="El titulo del libro")
    fecha_publicacion = models.DateField(verbose_name="La fecha en el fue publicado el libro")
    isbn = models.CharField(max_length=20,verbose_name="El ISBN del libro")
    
    def __str__(self):
        return self.titulo


class Editor(models.Model):
    nombre = models.CharField(max_length=50,help_text="El titulo del Editor")
    website = models.CharField(max_length=200,verbose_name="El website el Editor")
    email = models.CharField(max_length=200,verbose_name="El email del Editor")
    
    def __str__(self):
        return self.nombre

class Colaborador(models.Model):
    nombre = models.CharField(max_length=50,help_text="El nombre del colaborador")
    apellido = models.CharField(max_length=50,verbose_name="El apellido del colaborador")
    email = models.CharField(max_length=200,verbose_name="El email del colaborador")
    
    def __str__(self):
        return self.nombre
