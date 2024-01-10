from django.shortcuts import render
from mysite.models import Post
from mysite.models import User
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect,render, get_object_or_404, HttpResponseRedirect, reverse
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils import timezone
from .models import BorrowRecord 

def admin_books(request):
    books = Post.objects.all().order_by('slug')
    return render(request, 'admin_books.html', {'books': books})

def admin_books_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        write = request.POST.get('write')
        slug = request.POST.get('slug')
        pub_date = request.POST.get('pub_date')

        Post.objects.create(title=title,write=write, slug=slug, pub_date=pub_date)
        return redirect('admin_books')

    return HttpResponse("Invalid request method")

def admin_books_edit(request, slug):
    book = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.write = request.POST.get('write')
        book.slug = request.POST.get('slug')
        book.pub_date = request.POST.get('pub_date')
        book.save()
        return redirect('admin_books')

    return render(request, 'admin_books_edit.html', {'book': book})

def admin_books_delete(request, slug):
    print("Deleting book with slug:", slug)  # 添加这一行
    book = get_object_or_404(Post, slug=slug)
    book.delete()
    return redirect('admin_books')



def admin_books(request):
    books = Post.objects.all().order_by('slug')
    return render(request, 'admin_books.html', {'books': books})

def index(request, pid=None, del_pass=None):
    if request.user.is_authenticated:
        username = request.session.get('username')
    messages.get_messages(request)
    return render(request, 'index.html', locals())

def staffindex(request, pid=None, del_pass=None):
    if request.user.is_authenticated:
        username = request.session.get('username')
    messages.get_messages(request)
    return render(request, 'staffindex.html', locals())
        
def userindex(request, pid=None, del_pass=None):
    if request.user.is_authenticated:
        username = request.user.username
    messages.get_messages(request)
    return render(request, 'userindex.html', locals())

@login_required(login_url='/user_login/')
def userinfo(request):
    if request.user.is_authenticated:
        username = request.user.username
        try:
            userinfo = user.objects.get(username=username)
        except:
            pass
    return render(request, 'userinfo.html', locals())
    
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def user_login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            login_name = request.POST.get('username', '').strip()
            login_password = request.POST.get('password', '')
            user = authenticate(username=login_name, password=login_password)
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    print("success")
                    print(user.username)
                    request.session['username'] = user.username
                    if user.is_staff:
                            # 用户是工作人员，进入 staff.html
                        messages.success(request, '歡迎! 您的身分為 工作人員')
                        posts = Post.objects.all().order_by('pub_date')
                        return render(request, 'staffindex.html', {'posts': posts})
                    else:
                        # 用户不是工作人员，进入 user.html
                        posts = Post.objects.all().order_by('pub_date')
                        messages.success(request, '歡迎! 您的身分為 顧客')
                        return render(request, 'userindex.html', {'posts': posts})
                else:
                    messages.warning(request, '帳號尚未啟用')
            else:
                messages.warning(request, '登入失敗')
        else:
            messages.info(request, '帳號或密碼有誤')
    else:
        login_form = AuthenticationForm()
    
    return render(request, 'user_login.html', {'login_form': login_form})

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')  # 註冊成功後自動登入並重定向到首頁
    else:
        form = UserCreationForm()
    return render(request, 'user_register.html', {'form': form})

def user_logout(request):
    auth.logout(request)
    messages.add_message(request, messages.INFO, "登出成功了")
    return redirect('/')


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
    username = request.session.get('username')

    if not book.isBorrow:
        book.isBorrow = True
        book.save()
        BorrowRecord.objects.create(username = username, bookid = book.id, borrow_date = datetime.now())

    return HttpResponseRedirect(reverse('book_list'))

def return_book(request, book_id):
    book = get_object_or_404(Post, id=book_id)
    username = request.session.get('username')


    if book.isBorrow:
        book.isBorrow = False
        book.save()
        BorrowRecord.objects.filter(username = username, bookid = book.id).delete()
<<<<<<< HEAD

    return HttpResponseRedirect(reverse('book_list'))

from django.db.models import Q



def search_books(request):
    if 'q' in request.GET:
        query = request.GET['q']
        results =Post.objects.filter(title__icontains=query) 
        return render(request, 'search_results.html',{'results': results, 'query': query})
    else:
        return render(request, 'search_results.html')

=======

    return HttpResponseRedirect(reverse('book_list'))

from django.db.models import Q



def search_books(request):
    if 'q' in request.GET:
        query = request.GET['q']
        results =Post.objects.filter(title__icontains=query) 
        return render(request, 'search_results.html',{'results': results, 'query': query})
    else:
        return render(request, 'search_results.html')

<<<<<<< HEAD
=======
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

    
        
>>>>>>> a5247b8e6337e31a53a11be917503f2528d4201c
>>>>>>> f55f07ad9a867abd8275617248d902b5e596a7b0
