from pandas.io import json
import pandas as pd
from Trial1.settings import AUTH_PASSWORD_VALIDATORS
from Registeration.models import Account
from Registeration.forms import AccountForm
from django.http.response import HttpResponse, ResponseHeaders
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.views import APIView
from rest_framework import response
from rest_framework import serializers
from Registeration.serializer import RestAccountSerializer
from Registeration.models import JsonTab

# Create your views here.

#class SignupAPI(APIView):
#    serializer_class = RestAccountSerializer
#    def post(self, request, *args, **kwargs):
#        serializer = self.get_serializer(data = request.data)
#        serializer.isvalid(raise_exception = True)
#        return response({
#            'user' : RestAccountForm(user, context.self.get_serializer_context()).data,
#            'token' : AuthToken.objects.create(User)
#        })

def index(request):
        return render(request,'index.html')

def signup(request):
    form = AccountForm()
    context = {'form':form}
    if request.method == 'POST':
        form = AccountForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request,'auth-signup.html',context)
    else:
        return render(request,'auth-signup.html',context)
##############   
#    return render(request,'auth-signup.html', context)
#        username = request.POST.get('username')
#        email = request.POST.get('email')
#        password = request.POST.get('password')
#        print(email,password)
#        try:
#            User.objects.get(email = email)
#            return render (request,'auth-signup.html', {'error':'email exist'})
#        except User.DoesNotExist:
#            user = User.objects.create_user(username=username,password=password,email=email)
#            auth.login(request,user)
#            return render(request,'auth-signup.html')
#    else:
#        return render(request,'auth-signup.html')

class signinAPI(APIView):

    def post(self, request, format = None):
        data = self.request.data
        print(data)
        Users = auth.authenticate(email = data['email'], password = data['password'])
        if Users is not None:
            auth.login(request,Users)
            return HttpResponse('API is successful')
        else:
            return HttpResponse('auth-signin.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        Users = auth.authenticate(email = request.POST.get('email'), password = request.POST.get('password'))
        print(Users,email,password)

        if Users is not None:
            auth.login(request,Users)
            return render(request,'index.html')
        else:
            return render(request,'auth-signin.html')
    else:
        return render(request,'auth-signin.html')

#def Home(request):
#    if request.method == 'POST':
#        username = request.POST.get('username')
#        firstname = request.POST.get('firstname')
#        lastname = request.POST.get('lastname')
#        birthdate = request.POST.get('birthdate')
#        emial = request.POST.get('email')
#        password = request.POST.get('password')
#        Users = Register( username = username, firstname = firstname, lastname = lastname, birthdate = birthdate, emial = emial, password = password)
#        Users.save()
#        return render(request,'Home.html')
#    else:
#        return render(request,'Home.html')

class ReadingJason(APIView):
    def get(self, request, format = None):
        source = self.request.data
        body = pd.DataFrame(source)
        JsonTab.objects.bulk_create(JsonTab(**vals) for vals in body.to_dict('records'))
        return HttpResponse('API is successful')