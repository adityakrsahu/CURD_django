from django.shortcuts import render
from django.http import HttpResponse
from .models import Student,Query
from django.db.models import Q
# Create your views here.

# ****************************************for crud operation************************************************
 
# data save
def home(request):
    return render(request, "app/home.html")

def about(request):
    return render(request, "app/about.html")

def contact(request):
    return render(request, "app/contact.html")

def services(request):
    return render(request, "app/services.html")

def register(request):
        return render(request, "app/register.html")

def login(request):
        return render(request, "app/login.html")

def savedata(request):
     if request.POST:
          Name =request.POST["name"]
          Email =request.POST["email"]
          Contact =request.POST["contact"]
          City =request.POST["city"]
          Password =request.POST["password"]

          user =Student.objects.filter(Email=Email)
          if user:
            msg= "user already exist"
            return render(request, 'app/register.html', {'data': msg})

          else:
            Student.objects.create(
            Name=Name,
            Email=Email,
            Contact=Contact,
            City=City,
            Password=Password
           )
            msg="user creation successfuly"
            return render(request, 'app/login.html',{'data':msg})

     else:
         
        msg="change method again post"
        return render(request, "app/register.html")

def logindata(request):
    if request.method=='POST':
        Email=request.POST['email']
        Password=request.POST['password']
        user=Student.objects.filter(Email=Email)
        if user:
            data=Student.objects.get(Email=Email)
            if data.Password==Password:
                Name=data.Name
                Email=data.Email
                Contact=data.Contact
                City=data.City
                # print(Name)
                # print(Email)
                # print(Contact)
                # print(City)
                user={
                    'name':Name,
                    'email':Email,
                    'contact':Contact,
                    'city':City
                }
                return render(request,'app/dash.html',{'key':user})
            else:
                msg="password does nit match"
                return render(request,'app/login.html',{'ms':msg})
        else:
            msg="password does nit match"
            return render(request,'app/register.html',{'ms':msg})
        
        
def query(request):
    # Data come from HTML to View
    email = request.POST['email']
    query = request.POST['query']
    Query.objects.create(Email=email,Query=query)
    
    data = Student.objects.get(Email=email)
    Name = data.Name
    Email = data.Email
    Contact = data.Contact
    City = data.City
    user={
                    'name':Name,
                    'email':Email,
                    'contact':Contact,
                    'city':City
                }
    return render(request,'app/dash.html',{'key':user})


def showdata(request,pk):
    Querydata=Query.objects.filter(Email=pk)

    data = Student.objects.get(Email=pk)
    Name = data.Name
    Email = data.Email
    Contact = data.Contact
    City=data.City
    user={
        'name':Name,
        'email':Email,
        'contact':Contact,
        'city':City}
    
    return render(request,'app/showdata.html',{'key1':Querydata,'user':user})


def edit(request,pk):

    data=Query.objects.get(id=pk)
    email=data.Email
    query = data.Query
    id = data.id
    data1={
        'id':id,
        'email':email,
        'query':query
    }
    data = Student.objects.get(Email=email)
    Name = data.Name
    Email = data.Email
    Contact = data.Contact
    City=data.City
    user={
        'name':Name,
        'email':Email,
        'contact':Contact,
        'city':City                }
    return render(request,"app/dash.html",{'key':user,'key2':data1})


def update(request,pk):
    email = request.POST['email']
    query = request.POST['query']

    data = Query.objects.get(id=pk)
    data.Query = query
    data.Email = email
    data.save()
    data = Student.objects.get(Email=email)
    Name = data.Name
    Email = data.Email
    Contact = data.Contact
    City=data.City
    user={
        'name':Name,
        'email':Email,
        'contact':Contact,
        'city':City                }
    return render(request,"app/dash.html",{'key':user})


def delete(request,pk):
    # print(pk)
    data = Query.objects.get(id=pk)
    email = data.Email
    data.delete()
    data = Student.objects.get(Email=email)
    Name = data.Name
    Email = data.Email
    Contact = data.Contact
    City=data.City
    user={
        'name':Name,
        'email':Email,
        'contact':Contact,
        'city':City
                                                                 }
    return render(request,"app/showdata.html",{'key':user})

def search(request,pk):
    squery=request.POST['search']

    data = Student.objects.get(Email=pk)
    Name = data.Name
    email = data.Email
    Contact = data.Contact
    City=data.City
    password=data.Password

    user={
        'name':Name,
        'email':email,
        'contact':Contact,
        'city':City,
        'password':password}
    alldata=Query.objects.filter(Q(Email=email) & Q(Query=squery))
    return render(request,"app/showdata.html",{'key1':alldata,'user':user})