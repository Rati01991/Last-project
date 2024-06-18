from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('car/<int:car_id>/rent/', views.rent_car, name='rent_car'),
    path('car/post/', views.post_car, name='post_car'),
    path('car/<int:car_id>/update/', views.update_car, name='update_car'),
    path('car/<int:car_id>/delete/', views.delete_car, name='delete_car'),
]