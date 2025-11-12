from django.contrib import admin
from .models import ContactUs

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'service', 'address', 'created_at')
    list_filter = ('service', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone', 'address', 'service')
    readonly_fields = ('created_at', 'updated_at')
    list_per_page = 25
