from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import Request
from .forms import CreateNewRequest

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
        print(request.POST)
        
        return redirect('getRequests')
    
    else:
        return render(request, 'set_req.html', {
            'form': CreateNewRequest()
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
    
    return render(request, 'req.html', {
        'req': req
    })