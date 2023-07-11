from django.shortcuts import render, HttpResponse
from home.models import Contact

def home(request):
    return render(request,'home.html')
    

def about(request):
    # return HttpResponse("this is my About page")
    return render(request,'about.html')



def projects(request):
    # return HttpResponse("this is my Projects page")
    return render(request,'projects.html')



def contact(request):
    if request.method =="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        # print(name , email , phone, desc)
        contact = Contact(name=name, email=email, phone=phone,desc=desc)
        contact.save()
        print("the data has been written to the db")
        # return HttpResponse("this is my Contact page")
    return render(request,'contact.html')


