from django.shortcuts import render
from django.http import HttpResponse
import os
import joblib
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .forms import RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

model1 = joblib.load(os.path.dirname(__file__) + "\\mySVCModel1.pkl")
model2 = joblib.load(os.path.dirname(__file__) + "\\myModel4.pkl")


def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Save the form data to the database
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        
        # Optionally, add a success message
        messages.success(request, 'Your message has been sent successfully!')
        
        return redirect('contact')  # Redirect after POST
    
    return render(request, 'contact.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in after registration
            return redirect('home')  # Redirect to the homepage
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Step 3: Save the form data but don't commit yet
            user = form.save(commit=False)  # We stop the commit here so we can handle the password separately
            
            # Step 6: Hash the password
            user.password = make_password(form.cleaned_data['password'])  # Hash the password
            
            # Now commit and save the user with the hashed password
            user.save()

            return redirect('login')  # Redirect after successful registration
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        # Authenticate the user by email
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            # Log in the user
            login(request, user)
            return redirect('Index')  # Replace 'home' with the name of your home page view
        else:
            # Invalid login
            return render(request, 'login.html', {'error': 'Invalid email or password'})
    else:
        return render(request, 'login.html')

def index_view(request):
    return render(request, 'index.html')



"""def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the database
            return redirect('index')  # Redirect to a success page or contact page
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})"""


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def checkSpam(request):
    if(request.method == "POST"):
        finalAns = None
        algo = request.POST.get("algo")
        rawData=request.POST.get("rawdata")


        if(algo == "Algo-1"):
            finalAns = model1.predict([rawData])[0]
            param = {"answer" : finalAns}
        elif(algo == "Algo-2"):
            finalAns = model2.predict([rawData])[0]
            param = {"answer" : finalAns}


        return render(request, 'output.html', param)
    else:
        return render(request, 'index.html')
    