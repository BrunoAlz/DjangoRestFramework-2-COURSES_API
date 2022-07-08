from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib import messages

from accounts.forms import RegisterForm, UserAuthenticationForm


def user_register(request):

    user = request.user
    if user.is_authenticated:
        return redirect('core:index')

    if request.method == 'GET':
        form = RegisterForm()
        context = {
            'form': form
        }
        return render(request, 'accounts/register.html', context)

    if request.method == 'POST':
        form = RegisterForm(request.POST or None)

        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(
                request,
                f'Olá {user}, Sua conta foi criada e você será '
                f'redirecionado para o seu Profile.'
            )
            return redirect('accounts:login')

        else:
            context = {
                'form': form
            }
        return render(request, 'accounts/register.html', context)
    return render(request, 'accounts/login.html', {})


def user_login(request, *args, **kwargs):
    context = {}
    # user recebe uma instancia do usuario
    user = request.user
    # se a requisição for POST
    if request.method == 'POST':
        # form vai receber os dados do HTML passados via POST
        form = UserAuthenticationForm(request.POST or None)
        # se o form for Válido, verificações do DJANGO
        if form.is_valid():
            # pega o email do form via POST
            username = request.POST['username']
            # pega o password do form via POST
            password = request.POST['password']
            # user vai receber a authenticação que o django fará com os dados
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                #
                destination = get_redirect_if_exists(request)
                if destination:
                    return redirect(destination)
                return redirect('core:index')
        else:
            context['login_form'] = form

    return render(request, 'accounts/login.html', context)


def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get('next'):
            redirect = str(request.GET.get('next'))
    return redirect


def user_logout(request):
    logout(request)
    return render(request, 'accounts/logout.html')


def forgot_password(request):
    return render(request, 'accounts/forgot-password.html')


def confirm_email(request):
    return render(request, 'accounts/confirm-email.html')


def reset_password(request):
    return render(request, 'accounts/reset-password.html')


def lock_screen(request):
    return render(request, 'accounts/lock-screen.html')