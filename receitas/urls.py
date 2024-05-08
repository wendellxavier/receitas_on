from django.urls import path
from . import views


app_name = 'receitas'

urlpatterns = [
    path('', views.home, name='home'),
    path('receitas/<int:id_receitas>/', views.receitas_detalhe, name='receitas_detalhe'),
    path('receitas/category/<int:id_category>/', views.category, name='category'),
    path('receitas/search/', lambda request:..., name="search"),
    
]
