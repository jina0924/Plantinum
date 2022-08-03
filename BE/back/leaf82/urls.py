from django.urls import path
from . import views


urlpatterns = [
    path('', views.read_leaf82),
    path('<sido>/<sigungu>/', views.sido_sigungu_leaf82),
    path('new/', views.create_leaf82),
    path('search/sido/', views.search_sido),
    # path('search/neighborhood/', views.search_neighborhood),
    path('search/<sido>/sigungu/', views.search_sigungu),
]
