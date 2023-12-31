from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_items, name='items'),
    path('<int:item_id>/', views.item_detail, name='item_detail'),
    path('add/', views.add_item, name='add_item'),
    path('edit/<int:item_id>/', views.edit_item, name='edit_item'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('create_allergen/', views.create_allergen, name='create_allergen'),
    path(
        'delete_allergen/<int:allergen_id>/',
        views.delete_allergen,
        name='delete_allergen'
        ),
]
