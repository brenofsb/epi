from django.shortcuts import render, redirect
from nucleo.models import Colaborador, Equipamento, Emprestimo
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models.deletion import ProtectedError
from datetime import datetime
from django.utils import timezone

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

def equipa_editar(req, id):
    equipamento = get_object_or_404(Equipamento, id=id)

    if req.method == 'POST':
        nome = req.POST.get('nome', '')

        if not nome.strip():
            messages.error(req, 'Equipamento não atualizado! Preencher o campo: Nome')
            return redirect('equipa-editar', id=id)

        equipamento.nome = nome.strip()
        equipamento.save()
        messages.success(req, 'Equipamento atualizado com sucesso!')
        return redirect('equipa')

    return render(req, 'nucleo/equipamentos/editar.html', {
        'equipamento': equipamento,
    })

def equipa_excluir(req, id):
    equipamento = get_object_or_404(Equipamento, id=id)

    if req.method == 'POST':
        try:
            equipamento.delete()
        except ProtectedError:
            messages.error(req, 'Equipamento não pôde ser excluído: Associado a um empréstimo.')
        else:
            messages.success(req, 'Equipamento excluído com sucesso!')

    return redirect('equipa')

# Emprestimo
def emprest_criar(req):
    if req.method == 'POST':
        try:
            dt_emprest = timezone.make_aware(
                datetime.fromisoformat(req.POST.get('dt_emprest'))
            )
            dt_prev_devo = timezone.make_aware(
                datetime.fromisoformat(req.POST.get('dt_prev_devo'))
            )
        except (TypeError, ValueError):
            messages.error(req, 'Informe datas válidas para o empréstimo e a previsão de devolução.')
            return redirect('emprestimo-criar')

        if dt_prev_devo <= timezone.now():
            messages.error(req, 'A previsão de devolução deve ser posterior à data e hora atuais.')
            return redirect('emprestimo-criar')

        status = req.POST.get('status')
        status_validos = [
            valor for valor, texto in Emprestimo.status_choices[:2]
        ]

        if status not in status_validos:
            messages.error(req, 'Selecione um status válido para o cadastro.')
            return redirect('emprestimo-criar')

        colaborador = get_object_or_404(
            Colaborador,
            pk=req.POST.get('colaborador')
        )
        equipamento = get_object_or_404(
            Equipamento,
            pk=req.POST.get('equipamento')
        )

        Emprestimo.objects.create(
            colaborador=colaborador,
            equipamento=equipamento,
            dt_emprest=dt_emprest,
            dt_prev_devo=dt_prev_devo,
            status=status,
            condicoes=req.POST.get('condicoes', '').strip(),
        )

        messages.success(req, 'Empréstimo cadastrado com sucesso!')
        return redirect('emprestimo-criar')

    return render(req, 'nucleo/emprestimo/criar.html',
    {'colaboradores': Colaborador.objects.all(),
    'equipamentos': Equipamento.objects.all(),
    'status': Emprestimo.status_choices[: 2],
    })



