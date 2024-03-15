from django.shortcuts import redirect, render
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import *
# Create your views here.
def indexapp(req):
    if req.method == 'POST':
        recipename=req.POST['recipename']
        recipedesc=req.POST['recipedescription']
        recipeimg=req.FILES['recipeimage']

        recipe.objects.create(
            recipename=recipename,
            recipedescription=recipedesc,
            recipeimg=recipeimg
        )
       

    return render(req,'index.html')

def report(req):
    queryset=recipe.objects.all()
    queryset1=recipe.objects.all().count()
    return render(req,"report.html",context={"recipereport":queryset,"counter":queryset1})


def dele(req,id):
    queryset=recipe.objects.all().get(id = id)
    queryset.delete()
    return redirect("/report")

def updatee(req,id):
    queryset=recipe.objects.get(id = id)
    context={"recipe":queryset}
    if req.method == "POST":
        data = req.POST
        recipename=req.POST['recipename']
        recipedescription=req.POST['recipedescription']
        recipeimage=req.FILES.get('recipeimage')

        queryset.recipename=recipename
        queryset.recipedescription=recipedescription
        if recipeimage:
            queryset.recipeimg=recipeimage

        queryset.save()
        return redirect("/report")
        
    return render(req,"update.html",context)    


def login(req):
    return render(req,"login.html")

def register(req):
    if req.method == "POST":
        fname=req.POST.get('fname')
        username=req.POST.get('username')
        password=req.POST.get('password')

        user=User.objects.create(
            username=username,
            first_name=fname
                                 )
        user.set_password(password)
    return render(req,'register.html')