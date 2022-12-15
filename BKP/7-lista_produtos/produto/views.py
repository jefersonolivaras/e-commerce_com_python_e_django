from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from . import models

# Create your views here.


class ListaProdutos(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 3


class DetalheProduto(View):
    pass


class AddToCart(View):
    pass


class RemoveToCart(View):
    pass


class Carrinho(View):
    pass


class Finalizar(View):
    pass
