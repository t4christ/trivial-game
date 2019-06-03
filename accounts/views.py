from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from .models import MyUser




# def login_view(request):
# 	form = LoginForm(request.POST or None)
# 	next_url = request.GET.get('next')
# 	if form.is_valid():
# 		username = form.cleaned_data['username']
# 		password = form.cleaned_data['password']
		
# 		user = authenticate(username=username, password=password)
# 		if user is not None:
# 			login(request, user)
# 			if next_url is not None:
# 				return HttpResponseRedirect(next_url)
# 			return HttpResponseRedirect("/")
# 	title = "Login"
# 	context = {
# 		"form": form,
# 		"title": title,
# 		}
# 	return render(request, "login.html", context)
def login_view(request):
    form = LoginForm(request.POST or None)
    next_url =  request.GET.get('next')
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            # print("Last login", request.user.last_login)
            login(request,user)
            loyalty_point=request.user.loyalty_point
            loyalty_point +=100
            
            # print("Last login",request.user.last_login.strftime("%m-%d %H:%M:%S"))
            if request.user.last_login.strftime("%H") > "24":
                MyUser.object.filter(username=username).update(loyalty_point=loyalty_point)
                # print("Last login",request.user.last_login.strftime("%m-%d %H"))
            else:
                print("Not Yet Time to get points")
            if next_url is not None:
                return HttpResponseRedirect(next_url)
            return HttpResponseRedirect("/")
    title = "Login"
    context = {
        "form": form,
        "title":title,
    }
    return render(request, "login.html", context)







def register_view(request):
    where_from = request.META.get('HTTP_REFERER')
    current_site = request.META['HTTP_HOST']
    get_name = "%s/play_tap_tap/understand/"%current_site
    title="Register"

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username= form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data.get('password2')
        phone_number=form.cleaned_data['phone_number']
        first_name=form.cleaned_data['first_name']
        last_name=form.cleaned_data['last_name']
        if len(phone_number) > 13:
            messages.error(request,"Length of phone number exceeded.")
        else:
            new_user=MyUser()
            new_user.email=email
            new_user.first_name=first_name
            new_user.last_name=last_name
            new_user.username=username
            new_user.phone_number=phone_number
            new_user.set_password(password)
            new_user.save()
            messages.success(request,"Successfully Registered")
            return redirect("/login")
    context = {
        "form": form,
        "title": title
    }
    return render(request, "register.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")