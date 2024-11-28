from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from. models import Customer
from django.contrib import messages

from django.contrib.auth import authenticate,login,logout

# Create your views here.
def show_account(request):
    context={} # to identify active tab  # a javascript function is used in account.html to control this
# register section
    if request.POST and 'btn_register' in request.POST: # and 'btn_register' in request.POST -> to check request button is activated:
        context['register'] =True # this context to identify the active tab
        try:
            # print(request.POST)
            username=request.POST.get('username')
            password = request.POST.get('password')
            # name=  # this filed is not added
            email=request.POST.get('email')
            address=request.POST.get('address')
            phone=request.POST.get('phone')
        # create user account
            user=User.objects.create_user(

               username=username,
               password=password,
               email=email
            )
        #create customer account
            customer=Customer.objects.create(
                name=username,
               user=user,
               phone=phone,
               address=address
           )
            success_msg="User Registered Successfully"
            messages.success(request,success_msg)
            # return redirect('home')

        except Exception as e:
            error_message="Duplicate username or invalid inputs"
            messages.error(request,error_message)
# login section
    if request.POST and 'btn_login' in request.POST:  # and 'btn_register' in request.POST -> to check request button is activated:
        context['login'] = False # this context to identify the active tab

        username = request.POST.get('username')
        password = request.POST.get('password')
# check user is auth user

        user=authenticate(username=username,password=password) #,key= value
        if user :
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"invalid user credentials")



    return render(request,'account.html',context)

def signout(request):
    logout(request)
    return redirect('home')