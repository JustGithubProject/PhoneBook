from django.contrib import admin
from .models import Person, Phone


class PersonAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class PhoneAdmin(admin.ModelAdmin):
    list_display = ['phone', 'contact']
    search_fields = ['phone', 'contact']


admin.site.register(Person, PersonAdmin)
admin.site.register(Phone, PhoneAdmin)