from django.shortcuts import render
from info.models import Adress,UserProfile,Company
from django.contrib.auth.models import User
def index(request):
    informatii = []
    valori =[]
    user = request.user
    users = UserProfile.objects.all()
    for h in users:
        if(user.get_username() == h.user.get_username()):
            informatii.append(("ORAS ",h.adress.oras))
            informatii.append(("TARA ",h.adress.tara))
            informatii.append(("STRADA ",h.adress.strada))
            informatii.append(("ZIP CODE ",h.adress.zip_code))
            informatii.append(("COMPANY",h.company.name))
    for e in User.objects.all():
        valori.append(e.get_username())
    return render(request, 'personal/home.html',
                  {'content':[
                      informatii
                      ]})

def contact(request):
    return render(request, 'personal/basic.html',
                  {'content':['If you would like to contact me ,please email me'
                              ,'jsadjsa@gmail.com']})
