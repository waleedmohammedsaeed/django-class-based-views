from django.shortcuts import render
from django.contrib import admin

# Create your views here.



def  post_list(requset):
    #post_list = post.objects.all()
    return render(requset , 'post/list.html', {'post_list' : post_list})

def  post_detail(requset):
    pass    
