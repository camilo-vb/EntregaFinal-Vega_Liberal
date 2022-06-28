from django.urls import path
from country import views



urlpatterns = [
    path('country', views.country_list, name='countries'),
    path('country/add', views.country_form, name='country_form'),
    path('country/<int:pk>/update', views.update_country, name='country_update'),
    path('country/<int:pk>/delete', views.delete_country, name='country-delete'),
    ]