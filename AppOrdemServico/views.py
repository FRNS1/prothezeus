from django.shortcuts import render

# Create your views here.
def ordens_servico(request):

    context = {}

    return render(request, 'Pages/homeos.html', context)