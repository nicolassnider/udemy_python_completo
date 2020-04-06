from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.
def home(request):
    blogs= Post.objects.all()
    return render(request,"blog/home.html",{'blogs':blogs})

def blog(request,id):
    blog= Post.objects.get(id=id)
    return render(request,"blog/blog.html",{'blog':blog})
