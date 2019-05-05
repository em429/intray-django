from django.contrib import admin
from .models import Item

# Register your models here.


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    search_fields = ['item_uuid', 'item_text']
    list_display = ['item_uuid', 'timestamp', 'item_text']
    list_filter = ['timestamp']
