from django.forms import ModelForm
from .models import Room, User
from django.contrib.auth.forms import UserCreationForm

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'avatar', 'name', 'bio']
        

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__' # it like : ['name', 'description', 'created_at', 'updated_at' ,....]
        exclude = ['host', 'participants']

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'password1', 'password2']