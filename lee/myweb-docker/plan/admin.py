from django.contrib import admin
from plan.models import Plan
# Register your models here.

class PlanAdmin(admin.ModelAdmin):
    list_display = ['plan', 'detail', 'create_time', 'sys']


admin.site.register(Plan,PlanAdmin)
