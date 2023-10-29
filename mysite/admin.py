from django.contrib import admin
from mysite.models import Post

class PostAdmin(admin.ModelAdmin):    #管理者介面可以多看到這幾個
    list_display=('title','slug','pub_date')
    
# Register your models here.

admin.site.register(Post,PostAdmin)