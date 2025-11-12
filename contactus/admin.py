from django.contrib import admin
from .models import ContactUs, ZohoLeadLog

class ZohoLeadLogInline(admin.TabularInline):
    model = ZohoLeadLog
    extra = 0
    readonly_fields = ('status', 'response_code', 'message', 'created_at')
    can_delete = False

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'service', 'address', 'created_at')
    list_filter = ('service', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone', 'address', 'service')
    readonly_fields = ('created_at', 'updated_at')
    list_per_page = 25
    inlines = [ZohoLeadLogInline]


@admin.register(ZohoLeadLog)
class ZohoLeadLogAdmin(admin.ModelAdmin):
    list_display = ('contact', 'status', 'response_code', 'message', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('contact__email', 'message')
    readonly_fields = ('contact', 'status', 'response_code', 'message', 'created_at')
    list_per_page = 25
