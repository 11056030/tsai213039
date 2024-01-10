from django.db import models
from django.utils.translation import gettext as _



class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.IntegerField(unique=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    write = models.CharField(max_length=50, blank=True, default='')
    image_url = models.CharField(max_length=255, default='images/1.jpg')  # 指定默认值 # 存储图像路径或 URL
    bookstype=[("一般書籍","一般書籍"),("教學用書","教學用書")]
    category = models.CharField(max_length=20, choices=bookstype, default="一般書籍")
    intro = models.TextField(default="", blank=True)
    photolink = models.TextField(default="", blank=True)
    body = models.TextField()
    isBorrow = models.BooleanField(_("外借中"), default=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    @property
    def formatted_is_borrow(self):
        if self.isBorrow:
            return '<span style="color: white; background-color: #afb0b2; border: 1px solid white; padding: 3px; border-radius: 3px;">外借中</span>'
        else:
            return '<span style="color: white; background-color: #7fade5; border: 1px solid white;padding: 3px; border-radius: 3px;">可借閱</span>'

    formatted_is_borrow.fget.short_description = "外借狀態"
    
    class Meta:
        ordering = ['slug'] 
    def __str__(self):
        return self.title
    
class Product(models.Model):
    SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    sku = models.CharField(max_length=5)
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    size = models.CharField(max_length=1, choices=SIZES)

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1),
        ),
    ]

class User(models.Model):
<<<<<<< HEAD
    name = models.CharField(max_length=20, null=False)
    email = models.EmailField()
    password = models.CharField(max_length=20, null=False)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class BorrowRecord(models.Model):
    username = models.CharField(max_length=20, null=False, default='null')
    bookid = models.IntegerField(null=False, default=0)
    borrow_date = models.DateField()
=======
    
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
            return self.name
    
>>>>>>> a5247b8e6337e31a53a11be917503f2528d4201c
