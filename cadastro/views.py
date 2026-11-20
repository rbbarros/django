from django.shortcuts import redirect, render

def pagina_login(request):
    if request.method == 'POST':
        return redirect('home')

    return render(request, 'cadastro/login.html')

def pagina_home(request):
    return render(request, 'cadastro/home.html')