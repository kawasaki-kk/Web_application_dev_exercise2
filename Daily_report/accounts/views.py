from django.shortcuts import render
from django.contrib.auth.views import login
from django.contrib.auth.views import logout

# Create your views here.
def login_view(request):
    template_name = 'accounts/login.html'
    return login(request, template_name='accounts/login.html' )

def logout_view(request):
    template_name = 'accounts/logged_out.html'
    return logout(request, template_name='accounts/logged_out.html')

