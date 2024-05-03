from django.shortcuts import render
from utils.fake import make_receita
from django.http import HttpResponse
from .models import Receita


def home(request):
    receitas = Receita.objects.filter(is_published=True,).order_by('-id')
    return render(request, 'home.html', context={'receitas': receitas})


def category(request, category_id):
    receitas = Receita.objects.filter(category__id=category_id, is_published=True,).order_by('-id')
    return render(request, 'category.html', context={'receitas': receitas})


def receitas(request, id_receitas):
    return render(request, 'receitas.html', context={'is_detail_page': True})
