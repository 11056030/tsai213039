from django.shortcuts import render
from mysite.models import Post
from mysite.models import User
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from django.utils.text import slugify

# Create your views here.
def post_list(request):
    posts = Post.objects.all()  # 从数据库中检索帖子
    return render(request, 'your_template.html', {'posts': posts})

def homepage(request):
    # 从数据库中检索帖子并按发布日期从旧到新排序
    posts = Post.objects.all().order_by('pub_date')

    # 渲染模板并传递排序后的书籍列表
    return render(request, 'index.html', {'posts': posts})

def showpost(request,slug):
    try:
        post =Post.objects.get(slug=slug)
        if post !=None:
            return render(request, "post.html",locals())
        else:
            return redirect("/")
    except:
        return redirect("/")
    
def book_list(request):
    books = Post.objects.all()[::-1]
    return render(request, 'book_list.html', {'books': books})

def borrow_book(request, book_id):
    book = get_object_or_404(Post, id=book_id)

    if not book.isBorrow:
        book.isBorrow = True
        book.save()

    return HttpResponseRedirect(reverse('book_list'))

def return_book(request, book_id):
    book = get_object_or_404(Post, id=book_id)

    if book.isBorrow:
        book.isBorrow = False
        book.save()

    return HttpResponseRedirect(reverse('book_list'))

def login(request):
    return render(request, 'login.html')

def checkuser(request, username, password):
    user = get_object_or_404(User, name=username)
    if user.password == password:
        posts = Post.objects.all().order_by('pub_date')
        return render(request, 'index.html', {'posts': posts})
    else:
        return render(request, 'register.html')

    
        