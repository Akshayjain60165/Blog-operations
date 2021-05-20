from django.http.response import HttpResponse
from django.shortcuts import render
from random import randint
# Create your views here.
from .models import blog,blog_comments


def homepage(request):
    return render(request,'homepage.html')

def addblog(request):
   if request.method == 'POST':
        place = request.POST['place']
        title  =  request.POST['title']
        is_unique = True
        while is_unique == True: 
            pk = randint(1, 1999) # 19 digits: 1, random 18 digits
            is_unique = blog.objects.filter(id=pk).exists()
        p = blog(blog_id = pk , place = place, title = title)
        p.save()
        return HttpResponse('done')
        
        
   else:
        return render(request,'addblog.html')

def seeblogs(request):
    p = blog.objects.all()
    return render(request,'blogs.html',{'p':p})


def seebyid(request):
    if request.method == 'POST':
        id = int(request.POST['id'])
        p = blog.objects.get(blod_id = id)
        try :
            p = blog.objects.get(blod_id = id)
        except blog.DoesNotExist:
            p = None
        if p ==None:
            return HttpResponse('wrongid')
        return render(request,'blogs.html',{'p':p})
    else:
        return render(request,'seebyid.html')


def deletebyid(request):
    if request.method == 'POST':
        id = int(request.POST['id'])
        p = blog.objects.get(blod_id = id).delete()
        return HttpResponse('done')
    else:
        return render(request,'deletebyid.html')

def update(request):
    if request.method == 'POST':
        id = int(request.POST['id'])
        place = request.POST['place']
        title  =  request.POST['title']
        p = blog.objects.get(blog_id = id).update(blog_id = id , place = place, title = title)
        return HttpResponse('done')
        
        
    else:
        return render(request,'update.html')

def addcomment(request):
    if request.method == 'POST':
        id = int(request.POST['id'])
        comment  =  request.POST['comment']
        p = blog_comments(blog_id = id , comment = comment)
        p.save()
        return HttpResponse('done')
        
        
    else:
        return render(request,'addcomment.html')

def seecomment(request):
    if request.method == 'POST':
        id = int(request.POST['id'])
        p = blog_comments.objects.filter(blod_id = id)
        return render(request,'comments.html',{'p':p})
    else:
        return render(request,'seecomment.html')
