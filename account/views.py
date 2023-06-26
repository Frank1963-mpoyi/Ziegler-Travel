from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import UserLoginForm, UserRegisterForm
# from .models import Address


class UserRegisterView(View):
    template_name = 'account/register.html'
    
    def get(self, request, **kwargs):
        
        # address = Address.objects.values().first()
        
        form = UserRegisterForm
        
        context = {
            'page_name': 'user_register',
            # 'address': address,
            'register_form': form,
        }
        return render(self.request, self.template_name, context)

    def post(self, request, **kwargs):
        
        # address = Address.objects.values().first()
        
        form = UserRegisterForm(request.POST or None)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email
            user.is_active = True
            user.last_updated_by = user.username
            user.save()
            
            messages.success(request, f"{user.fullname} You are successfuly created your account.")
            return redirect("web:accounts:login")
        
        messages.warning(request, "You did not register please try again.")
        
        context = {
            'page_name': 'user_register',
            # 'address': address,
            'register_form': form,
            }
        
        return render(self.request, self.template_name, context)

class UserLoginView(View):
    template_name = 'apps/accounts/login.html'
    
    def get(self, request, **kwargs):
        
        # address = Address.objects.values().first()
        
        login_form = UserLoginForm
        
        context = {
            'page_name': 'user_login',
            # 'address': address,
            'login_form': login_form,
        }
        
        return render(self.request, self.template_name, context)

    def post(self, request, **kwargs):
        
        # address = Address.objects.values().first()
        
        form = UserLoginForm(request.POST or None)
        
        if form.is_valid():
            user_obj = form.cleaned_data.get('user_obj')
            login(request, user_obj)
            
            messages.success(request, f"Welcome!, {(user_obj.fullname).title()} to Acacia Health Center.")
            return redirect('web:home:home_view')
        
        messages.warning(request, "You are not login please check your credentials.")
        
        context ={
            'page_name': 'user_login',
            # 'address': address,
            'login_form': form
            }
        
        return render(self.request, self.template_name, context)

class UserLogoutView(View):
    template_name = 'apps/home/index.html'
    
    def get(self, request, **kwargs):
        
        logout(request)
        
        messages.info(request, f" You are loged out . Have a nice day !.")
        
        return redirect('web:home:home_view')
