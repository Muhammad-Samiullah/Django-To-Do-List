from django.contrib import admin
from .models import Todo


class TudoAdmin(admin.ModelAdmin):
    list_display = ('text', 'added_date')


admin.site.register(Todo, TudoAdmin)
