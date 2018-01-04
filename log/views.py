from django.shortcuts import render
from django.contrib.auth import logout


def logoutView(request):
        
        logout(request)
        return render(request, 'log/home.html')
