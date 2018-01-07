from django.shortcuts import render
from info import models
from django.contrib.auth.models import User
from personal.forms import PersonalForm
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

balanceAcconts = []
nameAcconts = []

def select(request):
    return render(request,'personal/createAcc.html')

def index(request):
    infoAdress = []
    infoAcconts = []
    user = request.user
    users = models.UserProfile.objects.all()
    acconts = models.Account.objects.all()
    for h in users:
        if(user.get_username() == h.user.get_username()):
            infoAdress.append(("ORAS",h.adress.oras))
            infoAdress.append(("TARA",h.adress.tara))
            infoAdress.append(("STRADA",h.adress.strada))
            infoAdress.append(("ZIP CODE",h.adress.zip_code))
            infoAdress.append(("COMPANY",h.company.name))

    nameAcconts.clear()
    balanceAcconts.clear()

    for h in acconts:
        if(user.get_username() == h.user.user.get_username()):
            nameAcconts.append(h.name)
            balanceAcconts.append(h.balance)

    return render(request, 'personal/home.html',
                  {'content':[
                      infoAdress
                      ],
                   'account':[
                        infoAcconts
                   ]})

def contact(request):
    return render(request, 'personal/basic.html',
                  {'content':['If you would like to contact me ,please email me'
                              ,'jsadjsa@gmail.com']})

def add_account(request):
    form = PersonalForm()
    if request.method == "POST":
        form = PersonalForm(request.POST)
        if form.is_valid():
            account_item = form.save(commit=False)
            account_item.save()
    return render(request, 'personal/homeform.html', {'form': form})

def get_data(request,*args,**kwargs):
    data = {
        "sales": 5,
        "customers": 1,
    }
    return JsonResponse(data) #return a respons in object form on site , not text

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        user = request.user
        acconts = models.Account.objects.all()

        for h in acconts:
            if (user.get_username() == h.user.user.get_username()):
                balanceAcconts.append(h.balance)
                nameAcconts.append(h.name)
        data = {
            "labels": nameAcconts,
            "dData": balanceAcconts,
            "pusi": 1000
        }
        return Response(data)