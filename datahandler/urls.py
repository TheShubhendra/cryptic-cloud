from django.urls import path
from . import views
urlpatterns  =[
  path("data",views.data,name="data"),
  path("save",views.save,name="save"),
  path("check",views.check,name="check") ,
  ]