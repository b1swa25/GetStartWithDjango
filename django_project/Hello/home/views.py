from django.shortcuts import render, HttpResponse  #render is used to render the templete

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
    return render(request, 'contact.html')