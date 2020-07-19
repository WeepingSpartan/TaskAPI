from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
from ratelimit.decorators import ratelimit
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required


# Create your views here.


def signup(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #create User
            user=form.save()
            login(request,user)
            return redirect('account:login')
    else:
        form = UserCreationForm()
    
    return render(request,'account/signup.html',{'form':form})



def loginform(request):

    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user= form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:

                return redirect('account:random')

    else:
        form= AuthenticationForm()
    return render(request,'account/login.html',{'form':form })

def logoutopp(request):
    if request.method=="POST":
        logout(request)
        return redirect('account:login')

@login_required (login_url='/account/login/')
@ratelimit(key='ip', rate='5/m', method=['GET', 'POST'])
def randomizer(request):
    was_limited = getattr(request, 'limited', False)
    if was_limited:
        raise PermissionDenied()
    else:
        return render(request,'account/random.html')

