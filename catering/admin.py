from django.contrib import admin
from .models import Item, Category, Allergen


admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Allergen)
