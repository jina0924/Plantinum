from django.urls import path
from . import views

urlpatterns = [
    path('', views.plants),
    path('myplant/', views.read_myplant),
    path('myplant/<plantname>/', views.create_myplant),
    path('search/<plantname>/', views.search),
    path('myplant/<int:plant_pk>/otp/', views.create_otp),
]
