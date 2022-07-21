from django.urls import path
from . import views

urlpatterns = [
    path('', views.plants),
    path('search/<plantname>/', views.search),
    path('myplant/', views.read_myplant),
    path('myplant/<plantname>/', views.create_myplant),
    path('myplant/<int:myplant_pk>/otp/', views.create_otp),
]
