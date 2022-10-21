from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django import forms
from .models import User, Message
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
 
User = get_user_model()

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'required':'', 
            'name': 'username',
            'id':'username',
            'type':'text', 
            'class':'form-input' ,
            'placeholder':'John Doe', 
            'maxlength':'16',
            'minlength':'6'   
        })
        self.fields['email'].widget.attrs.update({
            'required':'', 'name':"email", 'id':"email", 'type':"email" ,'class':"form-input", 'placeholder':"johndoe@mail.com"
        })
        self.fields['password1'].widget.attrs.update({
            'required':'', 'name':"password1" ,'id':"password1" ,'type':"password", 'class':"form-input",'placeholder':"password" ,'maxlength':"22" ,'minlength':"8"
        })
        self.fields['password2'].widget.attrs.update({
            'required':'', 'name':"password2" ,'id':"password2" ,'type':"password", 'class':"form-input",'placeholder':"password" ,'maxlength':"22" ,'minlength':"8"
        })
    
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('email','username', 'password1', 'password2')  
        
        def save(self, commit=True):
            user = super(SignUpForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user  
            
class UserChangeForm(UserChangeForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('email',)

class ContactForm(forms.ModelForm):
    body = forms.CharField(required=True)

    class Meta:
        model = Message
        exclude = ("user", )