from django.shortcuts import render, HttpResponse

def home(request):
    return render(request,'home.html')
    

def about(request):
    # return HttpResponse("this is my About page")
    return render(request,'about.html')



def projects(request):
    # return HttpResponse("this is my Projects page")
    return render(request,'projects.html')



def contact(request):
    # return HttpResponse("this is my Contact page")
    return render(request,'contact.html')


