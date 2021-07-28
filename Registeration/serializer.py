from django.forms import ModelForm
from Registeration.models import Account
from rest_framework import serializers

class RestAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username','email','password']
    def create(self, validated_data):
        user = Account.objects.creae_user(validated_data['username'],validated_data['email'],validated_data['password'])
        return user