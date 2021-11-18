from django.contrib import admin
from .models import BusinessUnit, Organization, ThirdParty

# Register your models here.
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "state", "country")


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(BusinessUnit)
admin.site.register(ThirdParty)
