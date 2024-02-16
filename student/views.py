from django.shortcuts import render,HttpResponsePermanentRedirect

# Create your views here.
def delete(request,id):
    if request.method == 'POST':
        dl = User.object.get(pk=id)
        dl.delete()
        return HttpResponsePermanentRedirect('/')