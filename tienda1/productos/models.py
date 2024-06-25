from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Estado(models.Model):
    """
    agotado o disponible
    """
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.estado

class Producto(models.Model):
    nombre = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=400)
    ref_categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    precio = models.IntegerField()
    stock = models.IntegerField()
    ref_estado = models.ForeignKey(Estado,on_delete=models.CASCADE)
    imagen = models.FileField(upload_to="productos/")
