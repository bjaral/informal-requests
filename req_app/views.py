import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import Request
from .forms import RequestForm

# Decorador para redirigir a la lista de solicitudes si el usuario ya está autenticado
def login_excluded(redirect_to_list):
    def _method_wrapper(view_method):
        def _arguments_wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                for redirect_to in redirect_to_list:
                    return redirect(redirect_to, username=request.user.username)
            return view_method(request, *args, **kwargs)
        return _arguments_wrapper
    return _method_wrapper

def home(request):
    return render(request, 'home.html')

@login_excluded(['getRequests', 'setRequest'])
def signin(request):
    
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm()
        })
        
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
        if user is not None:
            login(request, user)
            return redirect('getRequests')
        
        return render(request, 'login.html', {
            'form': AuthenticationForm(),
            'error': 'Usuario o contraseña incorrectos'
        })

@login_required(login_url='signin')
def setRequest(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            fecha_ocurrencia = form.cleaned_data['fecha_ocurrencia']
            new_request = Request(
                asunto = form.cleaned_data['asunto'],
                cliente = form.cleaned_data['cliente'],
                descripcion = form.cleaned_data['descripcion'],
                fecha_ocurrencia = fecha_ocurrencia,
                done = form.cleaned_data['done'],
                user = request.user
            )
            new_request.save()
            return redirect('getRequests')
    
    else:
        return render(request, 'set_req.html', {
            'form': RequestForm()
        })

@login_required(login_url='signin')
def getRequests(request):
    reqs = Request.objects.filter(user_id = request.user.id)
    solved_reqs = reqs.filter(done = True)
    pending_reqs = reqs.filter(done = False)
    
    return render(request, 'get_req.html', {
        'solved': solved_reqs,
        'pending': pending_reqs
    })
    
@login_required(login_url='signin')
def request(request, req_id):
    req = get_object_or_404(Request, pk=req_id)
    
    if request.method == 'POST':
        form = RequestForm(request.POST, instance=req)
        if form.is_valid():
            req = form.save(commit=False)
            req.save()
            return redirect('getRequests')
    else:
        form = RequestForm(instance=req)
    
    return render(request, 'req.html', {
        'req': req,
        'form': form
    })
    
def signout(request):
    logout(request)
    return redirect('home')

def deleteRequest(request, req_id):
    req = get_object_or_404(Request, pk=req_id)
    req.delete()
    return redirect('getRequests')