from django.contrib import admin
from .models import studentdata

admin.site.register(studentdata)

class studentadmin(admin.ModelAdmin):
    list_display='__all__'
    search_fields=['name','s_id']