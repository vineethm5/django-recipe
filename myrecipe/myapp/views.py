from django.shortcuts import render
from .models import *
from django.http import HttpResponse
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
    return render(req,"index.html")