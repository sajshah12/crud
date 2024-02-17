from django.shortcuts import render,HttpResponsePermanentRedirect
from .models import User
from .forms import Userregister

# Create your views here.
def add(request):
    st = User.objects.all()
    if request.method == 'POST':
        fm = Userregister(request.POST)
        if fm.is_valid():
            fm.save()
            fm = Userregister()
    else:
        fm = Userregister()
        return render(request,'add.html',{'form':fm,'stu':st})


def delete(request,id):
    if request.method == 'POST':
        dl = User.object.get(pk=id)
        dl.delete()
        return HttpResponsePermanentRedirect('/')