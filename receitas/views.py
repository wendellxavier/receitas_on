from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import Http404
from .models import Receita


def home(request):
    receitas = Receita.objects.filter(is_published=True,).order_by('-id')
    return render(request, 'home.html', context={'receitas': receitas})


def category(request, category_id):
    receitas = get_list_or_404(Receita, category__id=category_id, is_published=True)
    return render(request, 'category.html', context={'receitas': receitas, 'title': f'{receitas.first().category.name} - Categoria'})


def receitas_detalhe(request, id_receitas):
    receitas = Receita.objects.get(id=id_receitas)
    return render(request, 'receitas.html', context={'receitas': receitas,'is_detail_page': True})
