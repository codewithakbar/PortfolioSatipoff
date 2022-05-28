from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    path('<slug:category_slug>/', views.post_list, name='product_list_by_category'),


]
