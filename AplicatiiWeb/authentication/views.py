from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from AplicatiiWeb import settings


# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist!")
            return redirect('register')

        if User.objects.filter(email=email):
            messages.error(request, "Email already used!")
            return redirect('register')

        if len(username)>20:
            messages.error(request,f"Username is too big!")
            return redirect('register')

        if not username.isalnum():
            messages.error(request,"Username must contain letters!")
            return redirect('register')

        myuser = User.objects.create_user(username=username, email=email, password=password)
        myuser.save()

        messages.success(request, 'Your account has been created!')

        # # Welcome Email
        #
        # subject = "Welcome to my project site."
        # message = "Hello " + myuser.username + "!\n Your account has been created! \n\n Now you can login! \\Sincerely,\n Flavius!\n"
        # from_email = settings.EMAIL_HOST_USER
        # to_list = [myuser.email]
        #
        return render(request, 'registration/login.html')

    return render(request, 'registration/register.html')

def auth_user_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user=user)
            # return render(request, 'NotesApp/notes_index.html', {'username': username})
            return redirect('/notes/')

        else:
            messages.info(request, 'Username or password is incorrect!')

    context = {}
    return render(request, 'registration/login.html')

