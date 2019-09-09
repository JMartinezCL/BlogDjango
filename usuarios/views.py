from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import CreateView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .forms import RegistroForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout


# Create your views here.
def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        print("////////////",request.user.username)
        if form.is_valid():
            usuario = form.save(commit=False)
            print (usuario.username)
            if User.objects.filter(username__iexact=request.user.username).exists():
        	    #raise form.ValidationError('Username already exists')
        	    print("--YA EXISTE EL SUJETO--")
            else:
        	    print("--NO EXISTE EL SUJETO--")
            """usuario.username = request.user.username
            usuario.first_name = request.user.first_name
            usuario.last_name = request.user.last_name
            usuario.email = request.user.email
            usuario.password = request.user.password"""
            usuario.save()
            return redirect('post_list')
    else:
        form = RegistroForm()
        print("NO HAY NADAAAAAAAA")
    return render(request, 'usuarios/usuario.html', {'form': form})


"""class registro(CreateView):
	model = User
	template_name = "usuarios/usuario.html"
	form_class = RegistroForm
	succesS_url = reverse_lazy("/")
"""

def login(request):
    # Creamos el formulario de autenticación vacío
    print("TROLLOLOLOLOLOLO")
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "usuarios/login.html", {'form': form})

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')