from django.contrib import admin
from service.models import Contact
from django.contrib.auth.admin import UserAdmin

class ContactAdmin(admin.ModelAdmin):
    list_display=('username', 'email', 'message')
admin.site.register(Contact, ContactAdmin)

# Register your models here.
