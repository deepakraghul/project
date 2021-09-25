from django.shortcuts import render,redirect
from  .models import *
from  .forms import *

def shopf(request):
    a=shopform()
    if request.method=="POST":
        a=shopform(request.POST,request.FILES)
        if a.is_valid():
            a.save()
            return redirect('done')
        else:
            return redirect('shopf')
    else:
        a=shopform()
    return render(request,"cloth.html",{"a":a})

def done(request):
    b=shop.objects.all()
    c=shop.objects.get(id=2)
    d=shop.objects.filter(cloth_name="frocks")
    return render(request,"done.html",{"b":b,"c":c,"d":d})
