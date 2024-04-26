import time
import uuid
from django.contrib import messages
from userApp.models import UserProfile
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from userApp.forms import userRegisterForm, UserCreationForm # call userRegisterForm form forms.py
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .tokens import account_activation_token # call 

# login function
def user_login(request):
    
    if request.method ==  "POST":   # request = POST
        
        username =  request.POST["username"]   # get data from the input bar named username from user_login.html
        password = request.POST["password"]   # get data from the input bar named password from user_login.html
        
        user = authenticate(request, username=username, password=password)  # authenticate users with data from username and password
        
        if user is not None:  # data form username and password not none
            login(request, user)   # use function login  to login with username data and password data
            return redirect('/')  # return homepage
        else:
            messages.error(request, f'Account do not exit plz register')
    
    return render(request, 'user_login.html')  # render user_login.html

# logout function
def user_logout(request):  
    logout(request)  # using function logout to logout user with user's request
    return redirect('/') # return homepage

# activate account function 
def activate(request, uidb64, token):
    User = get_user_model() # returns the user class used in the application
    try:
        uid = force_str(urlsafe_base64_decode(uidb64)) # decodes a url encoded base64 string and converts it to a Unicode string
        user = User.objects.get(pk=uid) # get user by uid
    except(TypeError, ValueError, OverflowError, User.DoesNotExist): 
        user = None

    if user is not None and account_activation_token.check_token(user, token): # check token
        user.is_active = True  # se account active = True
        user.save() # active user
        
        user_profile = UserProfile.objects.create(user=user, is_verified=True, auth_token=token)

        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('success')
    else:
        messages.error(request, 'Activation link is invalid!')
    
    return redirect('home')

# send active email function
def activeEmail(request, user, to_email):
    
    mail_subjectt = "Activate your user account" # set mail title
    message = render_to_string("token.html", { # set mail content
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subjectt, message, to=[to_email]) # send mail with title and content to client's mail
    if email.send():    
        messages.success(
            request,
            f"Hello <strong style='color: #1b38de;'>{user}</strong>, please go to your email <strong style='color: #1b38de;>{to_email}</strong> and verify your email to login! <br> If you do not receive an email, please check your spam folder!",
            extra_tags="safe",
        )
    else:
        messages.error(request, f"Problem sending email to {to_email}, check if you typed it conrrectly.")

def acitve_success(request):
    return render(request, 'success.html')

# register function
def user_register(request):
    
    if request.user.is_authenticated:  # check user
        return redirect('/')
    
    if request.method == "POST": # POST request
        form = userRegisterForm(request.POST)  # add userRegisterForm to form
        if form.is_valid(): # check valid form (data input form client)
            user = form.save(commit=False)
            user.is_active=False # set account active = False
            user.save() # save account to database
            activeEmail(request, user, form.cleaned_data.get('email')) # call send active mail function
            
            return redirect('/')
        
        else:
            for error in list(form.errors.values()):
                print(error)
                
    else:
        form = userRegisterForm()
        
    return render(request, 'user_register.html', {'form': form})
