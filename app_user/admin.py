from django.contrib import admin

# Register your models here.
from .models import User, Client, EmployerAdmin, Vendor


class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'created_at']
    
class UserManager(admin.ModelAdmin):
    list_display = ['admin']

class Userclient(admin.ModelAdmin):
    list_display = ['admin']
    
class UserOfficer(admin.ModelAdmin):
    list_display = ['admin']


admin.site.register(User, UserAdmin)
admin.site.register(EmployerAdmin, UserManager)
admin.site.register(Client, Userclient)
admin.site.register(Vendor, UserOfficer)
