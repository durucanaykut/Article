from django.shortcuts import render
from writer import forms
from writer import models

def post_list(request):
    form=forms
    veri=models.Reporter.objects.all()
    if(request.method=='POST'):
        profession=request.POST['profession']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        ekle=models.Reporter(profession=profession,first_name=first_name,
                             last_name=last_name, email=email)
        ekle.save()
    return render(request, 'writer/post_list.html', locals())
