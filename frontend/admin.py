from django.contrib import admin

# Register your models here.
from .models import Equipments,EquipmentStatus

admin.site.register(Equipments)
admin.site.register(EquipmentStatus)