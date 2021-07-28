from django.forms import ModelForm
from Registeration.models import JsonTab
import pandas as pd

f = pd.read_json('C:/Users/Kunal Gawali/Python_Practice/Trial1/Registeration/sample.json')

JsonTab.objects.bulk_create(JsonTab(**vals) for vals in f.to_dict('records'))