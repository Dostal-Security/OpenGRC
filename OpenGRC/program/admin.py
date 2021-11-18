from django.contrib import admin

from .models import Program

# Register your models here.
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("name", "organization", "business_unit", "contact")


admin.site.register(Program, ProgramAdmin)
