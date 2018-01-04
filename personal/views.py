from django.shortcuts import render
from info.models import Adress,UserProfile,Company
from django.contrib.auth.models import User
def index(request):
    adress = list(Adress.objects.all())
    valori =[]
    for e in User.objects.all():
        valori.append(e.get_username())
    return render(request, 'personal/home.html',
                  {'content':[
                      valori
                      ]})

def contact(request):
    return render(request, 'personal/basic.html',
                  {'content':['If you would like to contact me ,please email me'
                              ,'jsadjsa@gmail.com']})
