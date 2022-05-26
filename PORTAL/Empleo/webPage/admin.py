from django.contrib import admin
from .models import Ciudad, TipoContrato, Oferta, Candidato, Tipo_doc


# Register your models here.
admin.site.register(Ciudad)
admin.site.register(Oferta)
admin.site.register(Tipo_doc)
admin.site.register(Candidato)
admin.site.register(TipoContrato)

