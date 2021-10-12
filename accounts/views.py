
from django.shortcuts import render,redirect, get_list_or_404
from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm
from . models import Profile
from django.contrib.auth import login ,authenticate
from .forms import UserForm , ProfileForm
from django.contrib.auth.decorators import login_required
# Create your views here.




def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('/products')
    else:
       form = UserCreationForm()
    context = {'form' : form}    
    return render(request,'registration/singnup.html',context)


@login_required(login_url='/accounts/login/')
def profile(request,slug):
    profile = get_list_or_404(Profile,slug=slug)
    context  = {'profile' : profile}
    return render(request,'registration/profile.html',context)




