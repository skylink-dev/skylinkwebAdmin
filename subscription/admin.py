from django.contrib import admin
from .models import EmailSubscription

@admin.register(EmailSubscription)
class EmailSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at', 'active')
    search_fields = ('email',)
    list_filter = ('active', 'subscribed_at')
