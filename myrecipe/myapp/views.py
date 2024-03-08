from django.shortcuts import render
from .models import *
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
    
    return render(req,"report.html",context={"recipereport":queryset})