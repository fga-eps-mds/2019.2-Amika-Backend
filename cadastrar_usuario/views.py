from django.shortcuts import render
from .models import User

def tela_de_cadastro(request):
    if request.method == "POST":
        form = SubForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.save()
            return redirect('tela_de_cadastro')

    else:
        form = SubForm()
    return render(request, 'cadastrar_usuario/tela_de_cadastro.html', {'form': form})




