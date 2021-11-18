from django.contrib import admin

from .models import Framework, Control

# Register your models here.
class ControlAdmin(admin.ModelAdmin):
    list_display = (
        "control_item_id",
        "control_item_title",
        "control_group_id",
        "control_group_title",
    )


admin.site.register(Framework)
admin.site.register(Control, ControlAdmin)
