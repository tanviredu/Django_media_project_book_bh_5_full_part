from django import forms
from django.contrib.auth.models import User
# for creating
from django.contrib.auth.forms import UserCreationForm
# for authenticating
from django.contrib.auth.forms import AuthenticationForm
# for editing
from django.contrib.auth.forms import UserChangeForm

from .models import UserProfile

class MyRegistrationForm(UserCreationForm):
    ## adding new email feature
    email = forms.EmailField(required=True)

    def __init__(self,*args,**kargs):
        super(MyRegistrationForm,self).__init__(*args,**kargs)
        self.fields['username'].widget.attrs = {'class': 'form-control',}
        self.fields['email'].widget.attrs = {'class': 'form-control',}
        self.fields['password1'].widget.attrs = {'class': 'form-control',}
        self.fields['password2'].widget.attrs = {'class': 'form-control',}

        #if you need any additional field
        # you can add here
        class Meta:
            model = User
            fields = ('username','email','password1','password2')


## create another form for user UserChangeForm

class UserProfileChange(UserChangeForm):

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password')


class ProfilePic(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['profile_pic',]
