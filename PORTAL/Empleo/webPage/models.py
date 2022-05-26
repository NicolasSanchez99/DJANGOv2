from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tipo_doc(models.Model):
    documento = models.CharField(max_length=20)

    def __str__(self):
        TipoDC = self.documento
        return str(TipoDC)


class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=10)

    def __str__(self):
        city = self.nombre
        return city

#RELACION USER
class Candidato(models.Model):
    numero_documento = models.CharField(max_length=20)
    primer_nombre = models.CharField(max_length=50)
    otros_nombres = models.CharField(max_length=50, null=True, blank=True)
    apellido1 = models.CharField(max_length=50)
    apellido2 = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    perfil = models.TextField(max_length=100)
    password = models.CharField(max_length=20)
    foto = models.ImageField(null=True,blank=True)
    #AREGLAR
    tipo_documento = models.ForeignKey(Tipo_doc, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, null=False, on_delete=models.CASCADE)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.numero_documento


class TipoContrato(models.Model):
    contrato = models.CharField(max_length=50)

    def __str__(self):
        contrato = self.contrato
        return contrato



class Oferta(models.Model):
    vacante = models.SmallIntegerField()
    salario = models.FloatField()
    descripcion = models.TextField(max_length=500)
    tipo_contrato = models.ForeignKey(TipoContrato, null=False, blank=True, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, null=False, blank=True, on_delete=models.CASCADE)
    estado = models.BooleanField(default=False)
    postulado = models.ManyToManyField(Candidato, through='Postulados')




    def __str__(self):
        cs = self.id
        return str(cs)


class Postulados(models.Model):
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE)
    fecha_postulacion= models.DateField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields= ['candidato','oferta'],name='unique_offer')
        ]
