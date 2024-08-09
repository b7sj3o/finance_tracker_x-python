from django import forms
from .models import User, Expense, Income, ExpenseType, IncomeType
from django.forms import ModelForm, ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import DateInput


class DateTypeInput(DateInput):
    input_type = "date"


class RegisterUserForm(UserCreationForm):
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(),
        strip=False,
    )
    password2 = forms.CharField(
        label='Підтвредження паролю',
        widget=forms.PasswordInput(),
        strip=False,
    )
    class Meta:
        model = User
        fields = ['username']

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        # self.fields['username'].widget.attrs['class'] = 'form-control'
        # self.fields['password1'].widget.attrs['class'] = 'form-control'
        # self.fields['password2'].widget.attrs['class'] = 'form-control'


class LoginUserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginUserForm, self).__init__(*args, **kwargs)
        
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ExpenseForm(ModelForm):
    use_limit_balance = forms.BooleanField(required=False, label="Використовувати лімітний баланс",)
    
    class Meta:
        model = Expense
        fields = ("amount", "expense_type", "time",)
        widgets = {'time': DateTypeInput(),}
        
    def __init__(self, *args, **kwargs):
        super(ExpenseForm, self).__init__(*args, **kwargs)
        
        
        for _, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
        
        self.fields['use_limit_balance'].widget.attrs['style'] = "width: 30px; height: 30px;"
        self.fields['use_limit_balance'].widget.attrs['class'] = ""


class ExpenseTypeForm(ModelForm):
    
    class Meta:
        model = ExpenseType
        fields = ("name",)

    def __init__(self, *args, **kwargs):
        super(ExpenseTypeForm, self).__init__(*args, **kwargs)
        
        
        for _, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class IncomeForm(ModelForm):
    class Meta:
        model = Income
        fields = ("amount", "income_type", "time")
        widgets = {'time': DateTypeInput(),}
        
    def __init__(self, *args, **kwargs):
        super(IncomeForm, self).__init__(*args, **kwargs)
        
        for _, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
        

class IncomeTypeForm(ModelForm):
    
    class Meta:
        model = IncomeType
        fields = ("name",)

    def __init__(self, *args, **kwargs):
        super(IncomeTypeForm, self).__init__(*args, **kwargs)
        
        for _, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


