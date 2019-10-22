from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import DocumentoForm
from . models import AgendaRealizar

# Create your views here.
def enviar_anexo(request):
    if request.method == "POST":
        form = DocumentoForm(request.POST, request.FILES)
        form.save()
        return redirect('listar_anexos')
    else: 
        form = DocumentoForm()
    return render(request, 'enviarArquivo.html', {'form': form})

def listar_anexos(request):
    anexos = AgendaRealizar.objects.all()
    return render(request, 'listar_anexos.html', {'anexos': anexos})
