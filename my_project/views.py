from django.shortcuts import HttpResponse, render, redirect
from django.conf import settings 
from django.core.mail import send_mail 

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def no_url(request, exception):
    return render(request, 'no_url.html')

def no_url2(request):
    return render(request, 'no_url.html')

def contact(request):
    try:
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        send_mail(f'mail from {name}',message, email, ['gandhimanan1810@gmail.com'])
        return redirect('/')
    except:
        return render(request, 'contact.html')