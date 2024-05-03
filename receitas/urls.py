from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('receitas/<int:id_receitas>/', views.receitas, name='receitas'),
    path('receitas/category/<int:id_category>/', views.category, name='category')
    
]
