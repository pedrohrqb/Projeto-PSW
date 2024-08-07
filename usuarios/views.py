from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.messages import constants

def cadastro(request): 
    """Cria o cadastro dos usuários."""
    # O if abaixo renderiza o html para o django.
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    # Nesse elif, a requisição é no modo POST.
    elif request.method == 'POST':
        # Abaixo as variaveis pega os dados fornecidos pelos usuários.
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        # Aqui o if faz uma verificação se a senha é igual a confirmar_senha, se for, cadastra, se não manda para página novamente.
        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas devem ser iguais.')
            return redirect('/usuarios/cadastro')
        
        # Aqui o if faz outra verificação se a quantidade de caracteres da senha for menor que 6, não cadastra.
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'A senha deve ser maior que 6 caracteres.')
            return redirect('/usuarios/cadastro')
        
        # Abaixo ele vai verificar se já existe esse username no banco de dados, se existir, não cadastra.
        users = User.objects.filter(username=username)
        if users.exists():
            messages.add_message(request, constants.ERROR, 'Este usuário já existe.')
            return redirect('/usuarios/cadastro')

        # Aqui adiciona os dados no banco, adicionando somente o username e senha.
        user = User.objects.create_user(
            username=username,
            password=senha
        )

        # Ao logar, redireciona o usuário para página 'logar'.
        return redirect('/usuarios/logar')

def logar(request):
    if request.method == 'GET':
        return render(request, 'logar.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(request, username=username, password=senha)
        if user:
            auth.login(request, user)
            return redirect('/empresarios/cadastrar_empresa')
        messages.add_message(request, constants.ERROR, 'Usuário ou Senha inválidos.')
        return redirect('/usuarios/logar')
    
    