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
    return render(request,'add_student.html',{'form':fm,'Stud':st})


def delete(request,id):
    if request.method == 'POST':
        dl = User.object.get(pk=id)
        dl.delete()
        return HttpResponsePermanentRedirect('/')
    

    

def update(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        sm = Userregister(request.POST,instance=pi)
        if sm.is_valid():
            sm.save()
    else:
        pi = User.objects.get(pk=id)
        sm = Userregister(instance=pi)
    return render(request, 'update_student.html',{'form':sm})    
   
