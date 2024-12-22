from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .models import TableHeader, TableRow, Category
from django.forms import modelformset_factory

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    ROLE_CHOICES = [
        ('user', 'User'),
    ]
    
    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        widget=forms.RadioSelect(),
        label='Role',
        initial='user',  # Set default to 'user' or 'admin' as needed
    )
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'role')

    def clean(self):
        cleaned_data = super().clean()
        # Optional: Additional validation for the form (e.g., check if passwords match)
        return cleaned_data
  
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'category_decription', 'user']  # include 'user'
        labels = {
            'category_name': "Bo'lim nomi",  
            'category_decription': "Bo'lim matni", 
        }
        widgets = {
            'category_name': forms.TextInput(attrs={'class': 'form-control'}), 
            'category_decription': forms.Textarea(attrs={  
                'class': 'form-control',
                'rows': 4,  
            }),
            'user': forms.HiddenInput(),  # Make the user field hidden in the form
        }

class TableHeaderForm(forms.ModelForm):
    
    class Meta:
        model = TableHeader
        fields = ['header_name', 'references_category']
    header_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
        

class TableRowForm(forms.ModelForm):
    class Meta:
        model = TableRow
        fields = ['row_name', 'references_category', 'header']
    row_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    
TableHeaderFormSet = modelformset_factory(
    TableHeader, form=TableHeaderForm, extra=1, can_delete=True
)

TableRowFormSet = modelformset_factory(
    TableRow, form=TableRowForm, extra=1, can_delete=True
)
