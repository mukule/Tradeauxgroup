from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.models import User



# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account succesfully created for { username } You can now Login')
            return redirect('login')
    else:
        form = UserRegisterForm
    return render(request, 'users/register.html', {'form':form})

# def index(request):
#     user = request.user
#     context = {'user': user}
#     return render(request, 'users/index.html', context)
