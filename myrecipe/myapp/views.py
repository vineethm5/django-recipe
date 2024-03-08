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
    queryset1=recipe.objects.all().count()
    return render(req,"report.html",context={"recipereport":queryset,"counter":queryset1})


def dele(req):
    if req.method == 'GET':        
        totr=int(req.GET['totalrow'])
        for i in range(1,totr):
            print(i)
            if req.GET['chek'] == '1':
                print("hi iam workiing")
                k=i
                uid=req.GET["k"]
                print(uid)
    return render(req,"report.html")