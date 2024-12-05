from django import forms
from .models import User, Task

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'password']

class UserChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name

class TaskForm(forms.ModelForm):
    user = UserChoiceField(
        queryset=User.objects.all(),
        empty_label="Select a user"
    )

    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True

    )
    cost = forms.DecimalField(
        widget=forms.TextInput(attrs={'type': 'number'}),
        max_digits=10,
        decimal_places=2,
        required=True
    )
    class Meta:
        model = Task
        fields = ['user', 'description', 'date', 'cost']