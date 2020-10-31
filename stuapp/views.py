from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
# from channels.auth import login,logout
from .EmailBackEnd import EmailBackEnd
# Create your views here.
# from .import EmailBackEnd



def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login_page.html')

def doLogin(request):
    if request.method != 'POST':
        return HttpResponse('Method Not allowed')
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        if user != None:
            login(request,user)
            return HttpResponse(request.POST.get('email')+ request.POST.get('password'))
        else:
            return HttpResponse('Invail LOgin')

def GetUserDetail(request):
    if request.user != None:
        return HttpResponse("user :"+ request.POST.get('email')+ "type :"+ request.user.user_type)
    else:
        return HttpResponse("Please Login User")

def logout_user(request):
    logout(request)
    return HttpResponse("Logout Successful!")
