from django.contrib import admin
from accounts.models import AllUsers
# Register your models here.
@admin.register(AllUsers)
class AdminNewUser(admin.ModelAdmin):
    list_display = ('user_name', 'email', 'is_staff')