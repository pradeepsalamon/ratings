import json
from django.shortcuts import render,HttpResponse,redirect
from . import models
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def ratingForm(requset):
    if requset.method == 'POST':
        name = requset.POST.get('name')
        rate = requset.POST.get('rating')
        comments = requset.POST.get('comments')
        appName= requset.GET.get('appName')
        if (comments):
            None
        else:
            comments='no comment'
        models.ratings.objects.create(name=name,rate=rate,comments=comments,appName=appName)
        return redirect('success')
    appName= requset.GET.get('appName')
    return render(requset,'form.html',{'appName':appName})


@login_required
def viewRatings(request):
    rates = models.ratings.objects.all().values()
    rates = list(rates)
    print(request.user.username)
    return render(request,'view.html',{'ratings':json.dumps(rates)})

def success(request):
    return render(request,'success.html')

def loginPage(request):
    context = {"error":""}
    if request.method == "POST":
        user = authenticate(request,username=request.POST['name'],password=request.POST['password'])
        if user is not None:
            login(request,user)
            return redirect('view/')
        
    return render(request,'login.html',context)

