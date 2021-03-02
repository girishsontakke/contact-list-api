from .models import Contacts
from django.contrib import admin

# Register your models here.


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ["firstname", "lastname", "phone_number", "owner"]
    search_fields = ["firstname", "lastname", "phone_number"]
    list_filter = ["firstname", "lastname", "owner", "phone_number"]
    list_per_page = 25
