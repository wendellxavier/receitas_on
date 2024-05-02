from django.shortcuts import render
from utils.fake import make_receita
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html', context={'receitas': make_receita()for _ in range(10)})


def receitas(request,id):
    return render(request, 'receitas.html', context={'is_detail_page': True})