from django.contrib import admin
from .models import BusinessUnit, Organization, ThirdParty, Contact

# Register your models here.
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "state", "country")


class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "Organization")


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(BusinessUnit)
admin.site.register(ThirdParty)
admin.site.register(Contact, ContactAdmin)
