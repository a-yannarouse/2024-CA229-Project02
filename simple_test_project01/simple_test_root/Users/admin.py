from django.contrib import admin
from .models import Users

class UserAdmin(admin.ModelAdmin):
    list_display = ('title','update_date')
    ordering = ('title',)
    search_fields = ('title',)

admin.site.register(Users, UserAdmin)