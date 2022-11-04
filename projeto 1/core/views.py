from django.shortcuts import render
from .models import Produto

# Create your views here.

def index(request):
    produtos = Produto.objects.all()
    context = {
        'teste': 'testando o context do Django.',
        'produtos': produtos
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')
