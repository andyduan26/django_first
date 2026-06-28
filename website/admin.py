from django.contrib import admin

from .models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'whatsapp', 'requirement')
    search_fields = ('name', 'email', 'whatsapp', 'requirement')
    list_display_links = ('id', 'name')
    ordering = ('-id',)
