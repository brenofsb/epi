from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_http_methods


def redirecionar_para_pagina_permitida(user):
    destinos = [
        ('nucleo.view_colaborador', 'nucleo-inicial'),
        ('nucleo.view_equipamento', 'equipa'),
        ('nucleo.view_emprestimo', 'emprest-listar'),
        ('nucleo.add_colaborador', 'nucleo-criar'),
        ('nucleo.add_equipamento', 'equipa-criar'),
        ('nucleo.add_emprestimo', 'emprestimo-criar'),
    ]

    for permissao, rota in destinos:
        if user.has_perm(permissao):
            return redirect(rota)

    return HttpResponseForbidden(
        'Sua conta não tem permissão para acessar nenhuma página do sistema.'
    )


@require_http_methods(["GET", "POST"])
def login_view(request):
    if request.method == 'GET':
        return render(request, 'login/index.html', {
            'next': request.GET.get('next', ''),
        })

    proximo = request.POST.get('next', '')
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        if proximo and url_has_allowed_host_and_scheme(
            proximo,
            allowed_hosts={request.get_host()},
            require_https=request.is_secure(),
        ):
            return redirect(proximo)

        return redirecionar_para_pagina_permitida(user)

    return render(request, 'login/index.html', {
        'next': proximo,
        'erro': 'Usuário ou senha inválidos.',
    })

@require_http_methods(["POST"])
def logout_view(req):
    logout(req)
    return redirect('auth-login')
