from django.shortcuts import render, HttpResponse  #render is used to render the templete
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html') # index.html is the name of templetes
   # return HttpResponse("This is Home page")

def about(request):
    #return HttpResponse("This is About page")
    return render(request, 'about.html') 

def services(request):
    #return HttpResponse("This is Services page")
    return render(request, 'services.html') 

def contact(request):
    #return HttpResponse("This is Contact page")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()

       # message framework added here
        messages.success(request, "your message has been sent!")

    return render(request, 'contact.html')