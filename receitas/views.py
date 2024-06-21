from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import Http404
from .models import Receita
from django.db.models import Q
from django.core.paginator import Paginator
from utils.pagination import make_pagination_range


def home(request):
    receitas = get_list_or_404(Receita.objects.filter(is_published=True).order_by('-id'))
    try:
        current_page = int(request.GET.get('page', 1))
    except ValueError:
        current_page = 1
    paginator = Paginator(receitas, 3)
    page_obj = paginator.get_page(current_page)
    
    pagination_range = make_pagination_range(paginator.page_range, 4, current_page)
    
    
    return render(request, 'home.html', context={'receitas': page_obj, 'pagination_range': pagination_range})


def category(request, category_id):
    receitas = get_list_or_404(Receita.objects.filter(category__id=category_id, is_published=True).order_by('-id'))
    return render(request, 'category.html', context={'receitas': receitas, 'title': f'{receitas[0].category.name} - Categoria'})


def receitas_detalhe(request, id_receitas):
    receita = get_object_or_404(Receita, id=id_receitas, is_published=True)
    return render(request, 'receitas.html', context={'receita': receita,'is_detail_page': True})

def search(request):
    search_term = request.GET.get('search', '').strip()
    if not search_term:
        raise Http404()
    
    receitas = Receita.objects.filter(Q(title__icontains=search_term) | Q(description__icontains=search_term)).order_by('-id')
    
    return render(request, 'search.html', {'receitas.title': f'Pesquisar por "{search_term}" |', 'search_term': search_term, 'receitas': receitas})
