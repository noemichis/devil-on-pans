from django.contrib import admin
from .models import HirePackage, HireRequest


class HirePackageAdmin(admin.ModelAdmin):
    list_display = (
        'package_name',
        'price',
        'image',
        'serves_nr_guests',
        'description',
    )

    ordering = ('package_name',)

    search_fields = ('package_name', 'price', 'serves_nr_guests', 'description')

class HireRequestAdmin(admin.ModelAdmin):
    list_display = (
        'replied',
        'id',
        'hire_package',
        'name',
        'email',
        'date',
        'comments',
    )

    ordering = ('replied', 'hire_package',)

admin.site.register(HirePackage, HirePackageAdmin)
admin.site.register(HireRequest, HireRequestAdmin)