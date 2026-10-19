from django.shortcuts import render, redirect
from nucleo.models import Colaborador, Equipamento
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

# Colaboradores
def home(req):
    busca = req.GET.get('q', '')
    colaboradores = Colaborador.objects.filter(nome__icontains=busca)
    return render(req, 'nucleo/index.html', {
        'colaboradores': colaboradores,
    })

def tela_criar(req):
    return render(req, 'nucleo/forms/criar.html')

def salvar(req):
    nome = req.POST.get('nome')
    telefone = req.POST.get('telefone', '')

    if not nome or not  nome.strip():
        messages.error(req, 'Colaborador não cadastrado! Preencher o campo: Nome')
        return redirect('nucleo-criar')

    Colaborador.objects.create(
        nome=nome.strip(),
        telefone=telefone
    )
    messages.success(req, 'Colaborador cadastrado com sucesso!')
    return redirect('nucleo-criar')

def editar(req, id):
    colaborador = get_object_or_404(Colaborador, id=id)

    if req.method == 'POST':
        colaborador.nome = req.POST.get('nome')
        colaborador.telefone = req.POST.get('telefone')
        colaborador.save()
        return redirect('nucleo-inicial')

    return render(req, 'nucleo/forms/editar.html', {
        'colaborador': colaborador,
    })

def excluir(req, id):
    colaborador = get_object_or_404(Colaborador, id=id)

    if req.method == 'POST':
        colaborador.delete()

    return redirect('nucleo-inicial')

# Equipamentos
def equipa (req):
    equipamentos = Equipamento.objects.all()
    return render(req, 'nucleo/equipamentos/listar.html', {
        'equipamentos': equipamentos,
    }) 

def equipa_criar (req):
    return render(req, 'nucleo/equipamentos/criar.html')

def equipa_salvar (req):
    nome = req.POST.get('nome')

    if not nome or not nome.strip():
        messages.error(req, 'Equipamento não cadastrado! Preencher o campo: Nome')
        return redirect('equipa-criar')

    Equipamento.objects.create(nome=nome.strip())
    messages.success(req, 'Equipamento cadastrado com sucesso!')
    return redirect('equipa-criar')

