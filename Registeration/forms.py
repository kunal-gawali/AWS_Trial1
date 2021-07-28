from django.forms import ModelForm
from Registeration.models import Account
from rest_framework import serializers

class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['username','email','password']
        #fields = '__all__'