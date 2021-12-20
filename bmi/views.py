from django import http
from django.shortcuts import render
from django.http import HttpResponse, request
from bmi.forms import BmiForm, ContactForm
from django.core.mail import message, send_mail


def home(request):
    return render(request, 'bmi/home.html')



def contact(request):
    if request.method =="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")
            subject = request.POST.get("subject")

            data = {
                "name":name,
                "email":email,
                "message":message,
                "subject":subject
            }

            message = '''
            New message: {}
            From: {}
            '''.format(data['message'], data['email'])
            
            #### enter yours mail into xxx
            send_mail(data['subject'], message, '',['xxx@gmail.com'])
        return render(request, 'bmi/contact.html',{})
    else:
        form = ContactForm()
    return render(request, "bmi/contact.html", {"form":form})

def services(request):
    return render(request, 'bmi/services.html')

def bmi(request):
    if request.method == "POST":
        form = BmiForm(request.POST)
        if form.is_valid():
            height = form.cleaned_data["height"]/100
            weight = form.cleaned_data["weight"]
            bmi = round(weight/height**2,2)
            return render(request, "bmi/bmi.html", {"form": form, "bmi": bmi})
    else:
        form = BmiForm()
    return render(request, "bmi/bmi.html", {"form": form})

def success(request):
        return render(request, 'bmi/success.html')

    


