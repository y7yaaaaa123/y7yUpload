from django.conf import settings
from django.shortcuts import redirect, render
from .forms import Uplode
from .models import *
from django.http import Http404, HttpResponse
import os
from django.shortcuts import render
from django.views.generic import ListView
import json



def tt(request):
    if request.POST:
        form= Uplode(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect(tt) 
    
    search=FilesAdmin.objects.all()
    context = {
        'file':search,
        'form':Uplode(),
        }
    context["qs_json"] = json.dumps(list(FilesAdmin.objects.values()))
    return render(request,'home.html',context)

def about(request):
    return render(request, 'About.html')

def my_view(request):
    # View code here...
    return render(request, '404.html')

# def tt(request):
#     if request.POST:
#         form= Uplode(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#         return redirect(tt) 
    
#     search=FilesAdmin.objects.all()
#     t=None
#     if 'search' in request.GET:
#         t=request.GET['search']
#         if t:
#             search=search.filter(t__icontains=t)
#     context = {
#         'file':search,
#         'form':Uplode(),
#         }
#     return render(request,'home.html',context)

def download(request, path):
    file_path=os.path.join(settings.MEDIA_Root,path)
    if os.path.exists(file_path):
        with open(file_path,'rb')as fh:
            response=HttpResponse(fh.read(),content_type='application/a')
            response['content-Disposition']='inline; filename='+os.path.basename(file_path)
            return response
    raise Http404
####################################################################
def demo(request):

    return render(request,'index.html')

