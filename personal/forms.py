from django.forms import ModelForm
from info.models import Account


class PersonalForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'
