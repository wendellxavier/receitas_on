from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import Http404
from .models import Receita


def home(request):
    receitas = get_list_or_404(Receita.objects.filter(is_published=True).order_by('-id'))
    return render(request, 'home.html', context={'receitas': receitas})


def category(request, category_id):
    receitas = get_list_or_404(Receita.objects.filter(category__id=category_id, is_published=True).order_by('-id'))
    return render(request, 'category.html', context={'receitas': receitas, 'title': f'{receitas[0].category.name} - Categoria'})


def receitas_detalhe(request, id_receitas):
    receita = get_object_or_404(Receita, id=id_receitas, is_published=True)
    return render(request, 'receitas.html', context={'receita': receita,'is_detail_page': True})

def search(request):
    return render(request, 'receitas/search.html')
