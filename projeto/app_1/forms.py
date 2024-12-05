from django import forms
from .models import User, Task
from django.utils import timezone

class UserForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)

    cpf = forms.CharField(max_length=11, required=True)

    email = forms.EmailField(required=True)

    join_date = (forms.DateField
        (
        initial=timezone.now(),
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True
    ))

    password = forms.CharField(widget=forms.PasswordInput, required=True)
    
    class Meta:
        model = User
        fields = ['name', 'cpf', 'email', 'password','join_date']


class UserDeleteForm(forms.Form):
    cpf = forms.CharField(max_length=11, required=True, label='CPF')

    def clean_cpf(self):
        data = self.cleaned_data['cpf']
        if not User.objects.filter(cpf=data).exists():
            raise forms.ValidationError("No user found with this CPF.")
        return data

class UserChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name

class TaskForm(forms.ModelForm):
    user = UserChoiceField(
        queryset=User.objects.all().order_by('name'),
        empty_label="Select a user"
    )

    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True
    )
    
    cost = forms.DecimalField(
        widget=forms.TextInput(attrs={'type': 'number', 'id': 'id_cost'}),
        max_digits=10,
        decimal_places=2,
        required=True
    )
    class Meta:
        model = Task
        fields = ['user', 'description', 'date', 'cost']