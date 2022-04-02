from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

from news.models import News
from .models import userInput, Contact
from .forms import inputForm, contact_form


# Create your views here.

def homepage(request):
    if request.user.is_authenticated:
        return redirect("user:userpage")
    else:
        return HttpResponseRedirect("/all_news")
        #return render(request=request, template_name='home.html')


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("user:userpage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password')
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                #messages.success(request, "You are now logged in as {username}")
                #messages.info(request, "Hello, " + username + ".  You are now logged in as, " + username)
                #messages.add_message(request, messages.ERROR,"You are now logged in as, " + {username})
                return redirect("user:userpage")
            else:
                messages.success(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    #messages.success(request, "You have successfully logged out.")
    #return redirect("news:news")
    return HttpResponseRedirect("/all_news")


def userpage_view(request):

    dse_news = News.objects.all()
    input = userInput.objects.all()
    
    user_name = request.user.get_username()
    context = {
        "dse": dse_news,
        "input": input,
        "logged_username": user_name,
    }
    return render(request=request, template_name='userPage.html', context=context)
    # return render(request, "userPage.html", context)
    


def user_form(request):
    if request.method == 'POST':
        form = inputForm(request.POST)
        form2 = AuthenticationForm(request, data=request.POST)
        # if form2.is_valid():
        # 	username = request.POST['username']
        if form.is_valid():

            # process form data
            obj = userInput()  # gets new object
            obj.username = request.user.get_username()
            obj.trading_code = form.cleaned_data['trading_code']

            # finally save the object in db
            obj.save()
            return HttpResponseRedirect('listed_company')
    else:
        form = inputForm()

    return render(request, 'userInput.html', {'form': form})


def company_view(request):
    input = userInput.objects.all()
    user_name = request.user.get_username()
    context = {
        "input": input,
        "logged_username": user_name,
    }
    return render(request=request, template_name='companies.html', context=context)



def delete_company(request, id):
    record = userInput.objects.get(id = id)
    record.delete()
    return redirect("user:companies")


def about_dse(request):
    return render(request, 'about_dse.html')







def contact(request):
    if request.method == 'POST':
        form = contact_form(request.POST)
        if form.is_valid():
            # process form data
            obj = Contact()  # gets new object
            obj.full_name = form.cleaned_data['full_name']
            obj.email = form.cleaned_data['email']
            obj.message = form.cleaned_data['message']

            # finally save the object in db
            obj.save()
            return HttpResponseRedirect('contact')
    else:
        form = Contact()

    return render(request, 'contact.html', {'form': form})

# def contact(request):
#     if request.method=='POST':
#         full_name=request.POST['full_name']
#         email=request.POST['email']
#         message=request.POST['message']
#         contact=Contact.objects.create(full_name=full_name,email=email,message=message)
#         messages.success(request,'Data has been submitted')
#     return render(request,'contact.html')


# from django.contrib.auth import get_user

# def user_form(request):
#     if request.method == 'POST':
#         form = inputForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('userpage')
#     else:
#         # Get the currently logged-in User.
#         user = get_user(request)
#         # Provide User as initial data to the form
#         form = inputForm(initial={'username': user})

#     return render(request, 'userInput.html', {'form': form})


# def userinput_view(request):
#     return render(request=request, template_name='userInput.html')
