from django.shortcuts import render , redirect
from django.http import HttpResponse 
from .models import Cloud
# Create your views here.
def register(request):
  if request.method == "POST" :
    cloudname = request.POST["cloudname"]
    cloudname = request.POST["cloudname"]
  else:
    return render(request,"register.html")
def login(request):
  if request.method == "POST" :
    cloudname = request.POST["cloudname"]
    
    clouds = Cloud.objects.all()
    for i in clouds:
      if i.cloudname == cloudname:
        request.session["cloudname"] = cloudname
        return redirect("data")
    return HttpResponse("bad")
  else:
    return render(request,"login.html",{"cloud_message":"Please enter your cloudname","key_message":"Enter key to decrypt the cloud"})
def logout(request):
  request.session["cloudname"] = None
  return redirect(home)
def home(request):
  return HttpResponse("home")
