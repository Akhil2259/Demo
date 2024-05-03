from django.shortcuts import render
from .models import mobiles
# Create your views here.
def details(request):
    if request.method=="GET":
        data=mobiles.objects.all()
        return render(request,"mobile.html",{'data':data})