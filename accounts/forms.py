from django import forms  
from .models import Account
from store.models import Product




class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder' : 'Enter Password'
    }))
    Confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : 'Confirm Password'
    }))
    class Meta:
        model = Account
        fields = ["first_name", "last_name", "phone_number", "email", "password"]

    def __init__(self, *args,**kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['place_holder']  = 'Enter First Name'
        self.fields['last_name'].widget.attrs['place_holder']  = 'Enter Last Name'
        self.fields['phone_number'].widget.attrs['place_holder']  = 'Enter Phone Number'
        for field in self.fields:
            self.fields[field].widget.attrs['class']  = 'form-control'    

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('password does not match')



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'slug', 'description', 'price', 'stock','images', 'is_available', 'category' ]


