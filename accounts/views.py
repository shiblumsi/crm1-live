from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import Group
from .models import *
from .forms import Orderform,Signup,Customerform,Addproduct
from .django_filters import Orderfilter
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorate import unauthenticated_user,allowed_user,admin_only




@unauthenticated_user
def signup(request):

        form = Signup(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create (
                user = user,
            )
            return redirect('login')
        context = {
            'form':form
        }
        return render(request,'registration.html',context)





def login_(request):

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                if request.user.is_superuser:
                    return redirect('home')
                else:
                    return redirect('user')
        context = {

        }
        return render(request, 'login.html', context)




def logout_(request):
    logout(request)
    return redirect('login')






@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def profile(request):
    user = request.user.customer
    form = Customerform(instance=user)
    if request.method == 'POST':
        form = Customerform(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
    context = {
        'form':form
    }
    return render(request,'profile_settings.html',context)





@login_required(login_url='login')
@admin_only
def addproduct(request):
    form = Addproduct()
    if request.method == 'POST':
        form = Addproduct(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product')
    context ={'form':form}
    return render(request,'addproduct.html',context)






@login_required(login_url='login')
@admin_only
def home(request):
    customer = Customer.objects.all()
    order = Order.objects.all()
    total_order = order.count()
    order_delivered = order.filter(status="delivered").count()
    order_pending = order.filter(status="pending").count()

    context ={
        "customers":customer,
        'orders':order,
        'total_order':total_order,'order_delivered':order_delivered,'order_pending':order_pending
    }

    return render(request,'deshbord.html',context)






@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def products(request):
    product = Product.objects.all()
    context = {'products':product}
    return render(request,'products.html',context)








@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def user_(request):
    u_orders = request.user.customer.order_set.all()
    print(u_orders)
    context = {'u':u_orders}
    return render(request,'user.html',context)







@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def customer(request,pk):
    customer = Customer.objects.get(id=pk)
    order = customer.order_set.all()
    myfilter = Orderfilter(request.POST,queryset=order)
    order = myfilter.qs
    context = {
        'customers':customer,'orders':order,'filter_form':myfilter
    }
    return render(request,'customer.html',context)





@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def createorder(request):
    form = Orderform()
    if request.method == 'POST':
        form = Orderform(request.POST)
        if form.is_valid():
            instant = form.save(commit=False)
            instant.user = request.user
            instant.save()
            print('dddd',instant.user)
            return redirect('home')
    context = {
        'form':form
    }
    return render(request,'createorder.html',context)





@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def updateorder(request,pk):
    order = Order.objects.get(id=pk)
    form = Orderform(instance=order)
    if request.method == 'POST':
        form = Orderform(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form':form
    }
    return render(request,'createorder.html',context)





@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def deleteorder(request,pk):
    order = Order.objects.get(id=pk)
    order.delete()
    return redirect('/')