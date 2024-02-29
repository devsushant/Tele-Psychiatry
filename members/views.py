from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from .models import *
from .validators import *
# Create your views here.
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage


def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not CustomUser.objects.filter(username = username).exists():
            messages.error(request, 'Invalid username')
            return redirect('/signin/')
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/signin/')
        
        else:
            login(request, user)
            return redirect('/dashboard/')


    return render(request, "signin.html")

# Register page
def signup(request): 

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
    
        try:
            validate_name(first_name)
            validate_name(last_name)
            validate_password(password)
            validate_email(email)
            validate_email_domain(email)

            # If all validations pass, create user or do further processing
            user = CustomUser.objects.create(
                first_name = first_name,
                last_name =last_name,
                email = email,
                phone = phone,
                username = username
                )            
        # Additional processing or redirecting can be done here
            user.set_password(password)
            user.save()

            messages.success(request, 'Account created successfully!')
            return redirect('signin')

        except ValidationError as e:
            messages.error(request, e.message)
            return redirect('signup')


        
    return render(request, 'signup.html')

def signout(request):

    logout(request)

    return redirect('/signin/')

@login_required(login_url = '/signin/')
def dashboard(request):
    return render(request, "dashboard.html")


def landing_page(request):
    return render(request, "landingpage.html") 

@login_required(login_url = '/signin/')
def profile_page(request):
    return render(request, "profile.html") 

@login_required(login_url = '/signin/')
def quicktest(request):
    return render(request, "quicktest.html")

@login_required(login_url = '/signin/')
def specialists(request):
    doctor =  DoctorInfo.objects.all()
    return render(request, "specialists.html", {'doctors': doctor})  

@login_required(login_url = '/signin/')
def appointments(request, id):
    return render(request, "appointments.html", {"id": id})

@login_required(login_url = '/signin/')
def Analyze(request):
    return render(request, "Analyze.html")

@login_required(login_url = '/signin/')
def Editprofile(request):
    return render(request, "Editprofile.html")
@login_required(login_url = '/signin/')
def quicktest1(request):
    return render(request, "quicktest1.html")

@login_required(login_url = '/signin/')
def send_email_view(request):
    if request.method == 'POST':
        email_subject = request.POST.get('emailsubject')
        message = request.POST.get('message')
        id=request.POST.get("doctorid")
        doctor = DoctorInfo.objects.get(pk=id)
        

        # recipient_email = 'sushantbhandari42@gmail.com'  # Specify the recipient's email address here
        patientemail= request.user.email
        
        # send_mail (
        #     email_subject,
        #     message,
        #     'settings.EMAIL_HOST_USER',# Your Email
        #     # user.email,
        #     [
        #         doctor.email
        #     ],
        #     headers={'Reply-To': patientemail},
        #     # user.email,  # The email you're sending from (defined in your settings)
        #     # [recipient_email],

        #     fail_silently=False,
        # )
        email = EmailMessage(
                subject=email_subject,
                body=message,
                from_email='settings.EMAIL_HOST_USER',  # From email
                to=[doctor.email],  # To email
                headers={'Reply-To': patientemail}  # Include a Reply-To header
            )

        email.send(fail_silently=False)
        messages.success(request, "Email sent successfully.")
        return redirect("/specialists/")
    else:
        # If not a POST request, just render a blank form or redirect as needed
        return render(request, '/profile/')
        
        
        
        
        
        
        
        
        
        
        
        
