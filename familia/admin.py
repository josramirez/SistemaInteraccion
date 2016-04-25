from django.contrib import admin

# Register your models here.
from familia.models import Hijo

class AdminHijo(admin.ModelAdmin):
    search_fields = ('nombre', 'fechaNacimiento')
    list_filter = ('nombre', 'talla')

admin.site.register(Hijo, AdminHijo)