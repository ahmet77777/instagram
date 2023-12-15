from django.shortcuts import render,redirect
from main.forms import LoginForm
def index(request):
    form = LoginForm()
    a=0
    if request.method == 'POST':
        LoginForm(request.POST).save()
        a=1
    context = {'form':form,'a':a}
    return render(request,"index.html",context)

def error(request):
    return render(request,"404.html")
def register(request):
    return render(request,"register.html")
# def index2(request):
#     form = LoginForm()
#     context = {'form':form}
#     return render(request,"index2.html",context)
# def save(request):
#     LoginForm(request.POST).save()
#     return redirect('/login/')


# Create your views here.
