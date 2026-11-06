from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def login_view(request):
    if request.method == 'GET':
        return render(request, 'login/index.html')

    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    print('User', user)
    if user is not None:
        login(request, user)
        return redirect('nucleo-inicial')
    else:
        # 
        return redirect('auth-login')

def logout_view(req):
    logout(req)
    return redirect('auth-login')
