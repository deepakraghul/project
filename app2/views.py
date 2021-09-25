from django.shortcuts import render
from .form import supermarket
from .models import supermarketsale




def market(request):
    form=supermarket()
    name=None
    total_price=0
    quantity=0
    food_menu=None
    if request.method=="POST":
        form=supermarket(request.POST,request.FILES)
        if form.is_valid():
            email=form.cleaned_data.get('email')
            name=form.cleaned_data.get('name')
            quantity=form.cleaned_data.get('quantity')
            price=form.cleaned_data.get('price')
            food_menu=form.cleaned_data.get('food_menu')
            total_price=quantity*price
            data=supermarketsale.objects.create(c_name=name,t_price=price)
            data.save()
            print(email)
            print(name)
            print(total_price)
    return render(request,"market.html",{'form':form,'name':name,'t':total_price,'f':food_menu,'q':quantity})






# Create your views here.
