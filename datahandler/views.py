from django.shortcuts import render, redirect
from accounts.models import Cloud
from django.http import HttpResponse
# Create your views here.
def data(request):
  cloudname = request.session["cloudname"]
  if cloudname is None:
    return redirect("login")
  else:
    cloud = Cloud.objects.get(cloudname=cloudname)
    data = cloud.data
    return render(request,"data.html",{"data":data,"cloud":cloudname})
def save(request):
  cloudname = request.session["cloudname"]
  data = request.POST["data"]
  try:
    cloud = Cloud.objects.get(cloudname=cloudname)
    cloud.data = data
    cloud.save(update_fields=["data"])
    return HttpResponse("1")
  except:
    return HttpResponse("0")
def check(request):
  if not request.method  == "POST":
    return HttpResponse("<h1>Bad Request</h1>")
  else:
    cloudname = request.POST["cloudname"]
    clouds = Cloud.objects.all()
    for i in clouds:
      if i.cloudname == cloudname:
        return HttpResponse("1")
    return HttpResponse("0")