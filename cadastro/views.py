from django.shortcuts import render

def pagina_login(request):
    return render(request, 'cadastro/login.html')
