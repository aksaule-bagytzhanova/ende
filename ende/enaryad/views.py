from django.db import connection
from django.shortcuts import render, redirect
from django.urls import path
from .models import *
from django.contrib.auth.models import Group
from .forms import OrderForm, EmployeeForm, CreateNar1Form
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users, unauthenticated_user, admin_only


# Create your views here.

@login_required(login_url='login')
def mainpage(request):

    return render(request, 'mainpage.html')


@login_required(login_url='login')
def enar(request):
    
    return render(request, 'enar.html')



@login_required(login_url='login')
def create_nar_page1(request):
    form = CreateNar1Form()
    
    if request.method == 'POST':
        
        form = CreateNar1Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_page')


    context={'form':form}
    return render(request, 'create_nar_page1.html', context)



@login_required(login_url='login')
def open_nar_page1(request):

    show_nar = create_e_naryad_table_1.objects.all()
    number = create_e_naryad_table_1.objects.count()

    context={'show_nar':show_nar, 'number':number}
    return render(request, 'open_nar_page1.html', context)



@login_required(login_url='login')
def close_nar_page1(request):
    return render(request, 'close_nar_page1.html')



@login_required(login_url='login')
def order_index(request):
    orders = Order.objects.all()

    

    context={'orders':orders}
    return render(request, 'order/order_index.html', context) 



@login_required(login_url='login')
def order_edit(request, pk):

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order) 

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_i')

    context={'form':form}
    return render(request, 'order/order_add.html', context)


@login_required(login_url='login')
def order_add(request):

    form = OrderForm()
    
    
    if request.method == 'POST':
        # print('Printing POST: ', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_i')


    context={'form':form}
    return render(request, 'order/order_add.html', context)


@login_required(login_url='login')
def passport_i(request):
    return render(request, 'passport/passport_index.html')



@login_required(login_url='login')
def passport_cabel(request):
    return render(request, 'passport/passport_cabel.html')



@login_required(login_url='login')
def passport_circuit(request):
    return render(request, 'passport/passport_circuit.html')



@login_required(login_url='login')
def passport_distribution(request):
    return render(request, 'passport/passport_distribution.html')



@login_required(login_url='login')
def passport_blade(request):
    return render(request, 'passport/passport_blade.html')



@login_required(login_url='login')
def passport_indoor(request):
    return render(request, 'passport/passport_indoor.html')



@login_required(login_url='login')
def passport_isg(request):
    return render(request, 'passport/passport_isg.html')



@login_required(login_url='login')
def passport_list(request):
    return render(request, 'passport/passport_list.html')



@login_required(login_url='login')
def passport_mcc(request):
    return render(request, 'passport/passport_mcc.html')



@login_required(login_url='login')
def passport_motor(request):
    return render(request, 'passport/passport_motor.html')



@login_required(login_url='login')
def passport_panel(request):
    return render(request, 'passport/passport_panel.html')



@login_required(login_url='login')
def passport_pg(request):
    return render(request, 'passport/passport_panel.html')



@login_required(login_url='login')  
def passport_substation(request):
    return render(request, 'passport/passport_substation.html')


@login_required(login_url='login')
def passport_uts(request):
    return render(request, 'passport/passport_uts.html')



@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
            
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('enar')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context ={}          
    return render(request, 'login.html',context)



def logOutPage(request):
    logout(request)
    return redirect('login')



@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def employee(request,pk_test):
    employee = Employee.objects.filter(id=pk_test)
    context={'employee':employee}
    return render(request, 'employee.html', context)



@login_required(login_url='login')
def plan_index(request):
    return render(request, 'plan/plan_index.html')



@login_required(login_url='login')
def messages_index(request):
    return render(request, 'messages/mess_index.html')


@login_required(login_url='login')
def accountSettings(request):
    employee=request.user.employee
    form = EmployeeForm(instance=employee)
    context={'form':form}
    return render(request, 'accountSettings.html', context)

