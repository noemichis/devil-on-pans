from django.contrib import admin
from .models import HirePackage


class HirePackageAdmin(admin.ModelAdmin):
    list_display = (
        'package_name',
        'price',
        'image',
        'serves_nr_guests',
        'description',
    )

    ordering = ('package_name')

    search_fields = ('package_name', 'price', 'serves_nr_guests', 'description')

admin.site.register(HirePackage)