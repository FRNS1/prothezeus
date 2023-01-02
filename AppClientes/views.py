from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from .filters import *
from .forms import *
from .models import *

# Create your views here.


def ClientesLab(request):

    cliente_filter = FilterClientes(
        request.GET, queryset=clientes.objects.all())

    paginated_notas = Paginator(cliente_filter.qs, 10)
    page_number = request.GET.get('page')
    cliente_obj = paginated_notas.get_page(page_number)

    context = {'cliente_filter': cliente_filter, 'cliente_obj': cliente_obj}

    return render(request, 'Pages\clientes.html', context)


def ClientesCad(request):

    form = CadastrarCliente(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('AppClientes:ClientesLab')

    context = {'form': form}

    return render(request, 'Pages\cadastroclientes.html', context)
