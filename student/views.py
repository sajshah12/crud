from django.shortcuts import render,HttpResponsePermanentRedirect
from .models import User
from .forms import Userregister

# Create your views here.
def delete(request,id):
    if request.method == 'POST':
        dl = User.object.get(pk=id)
        dl.delete()
        return HttpResponsePermanentRedirect('/')
