from django.contrib import admin
from apteks.models import Apteka

@admin.register(Apteka)
class AptekaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'contact_number', 'pharmacy_number')
    search_fields = ('pharmacy_number',)
