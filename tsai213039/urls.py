"""
URL configuration for tsai213039 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mysite import views as mv
<<<<<<< HEAD
from mysite.views import book_list, borrow_book, return_book,user_login,user_logout,user_register,search_books,admin_books, admin_books_add, admin_books_edit, admin_books_delete
from django.urls import path

=======
<<<<<<< HEAD
from mysite.views import book_list, borrow_book, return_book,user_login,user_logout,user_register,search_books,admin_books, admin_books_add, admin_books_edit, admin_books_delete
from django.urls import path

=======
<<<<<<< HEAD
from mysite.views import book_list, borrow_book, return_book,user_login,user_logout,user_register,search_books,admin_books, admin_books_add, admin_books_edit, admin_books_delete
from django.urls import path

=======
from mysite.views import book_list, borrow_book, return_book, login
>>>>>>> a5247b8e6337e31a53a11be917503f2528d4201c
>>>>>>> f55f07ad9a867abd8275617248d902b5e596a7b0
>>>>>>> 30ebf8d9e29b23ad8e00759559f0b8d87680f7ee

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",mv.homepage, name="homepage"),
    path("post/<slug:slug>/",mv.showpost,name="showpost"),
    path('book_list/', book_list, name='book_list'),
    path('user_logout/',user_logout, name='user_logout'),
    path('user_login/', user_login, name='user_login'),
    path('user_register/', user_register, name='user_register'),
    path('borrow/<int:book_id>/', borrow_book, name='borrow_book'),
    path('return/<int:book_id>/', return_book, name='return_book'),
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> f55f07ad9a867abd8275617248d902b5e596a7b0
>>>>>>> 30ebf8d9e29b23ad8e00759559f0b8d87680f7ee
    path('search_books/', search_books, name='search_books'),
    path('admin_books/', admin_books, name='admin_books'),
    path('admin_books/add/', admin_books_add, name='admin_books_add'),
    path('admin_books/edit/<slug>/', admin_books_edit, name='admin_books_edit'),
    path('admin_books/delete/<slug>/', admin_books_delete, name='admin_books_delete'),

<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
    path('login/', login, name="login"),
]
>>>>>>> a5247b8e6337e31a53a11be917503f2528d4201c
>>>>>>> f55f07ad9a867abd8275617248d902b5e596a7b0
>>>>>>> 30ebf8d9e29b23ad8e00759559f0b8d87680f7ee

]