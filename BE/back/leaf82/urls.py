from django.urls import path
from . import views


urlpatterns = [
    # path('', views.read_leaf82),
    path('main', views.Leaf82ListAPI.as_view()),
    # path('<sido>/<sigungu>/', views.sido_sigungu_leaf82),
    path('new/', views.create_leaf82),
    path('search/sido/', views.search_sido),
    path('search/<sido>/sigungu/', views.search_sigungu),
    # path('search', views.search),
    path('search', views.SearchAPI.as_view()),
    path('<username>/<int:posting_addr>/', views.detail_update_delete),

]
