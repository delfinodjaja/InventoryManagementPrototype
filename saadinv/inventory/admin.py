from django.contrib import admin
from .models import inventoryItem,category,patient_log,treatement_category,type

# Register your models here.
admin.site.register(inventoryItem)
admin.site.register(category)
admin.site.register(patient_log)
admin.site.register(treatement_category)
admin.site.register(type)
admin.site.site_header = 'Vet Care Admin'
