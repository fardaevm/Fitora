from django.contrib import admin
from .models import Weight
# Register your models here.

class WeightAdmin(admin.ModelAdmin):
    fields = (
        'user', 'weight', 'created_at', 'updated_at'
    )
    list_display = ('user', 'weight', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Weight, WeightAdmin)
