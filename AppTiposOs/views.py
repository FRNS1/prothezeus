from django.shortcuts import redirect, render

from .forms import *
from .models import *


# Create your views here.
def TipoOS_home(request):

    form_os = CadastrarServico(request.POST or None)
    if form_os.is_valid():
        form_os.save()
        return redirect('LoginPage:homepage')

    context = {'form_os': form_os}
    return render(request, 'Pages/tipoos.html', context)
