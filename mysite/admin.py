from django.contrib import admin
from mysite.models import Post, User,BorrowRecord

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'write','slug', 'pub_date', 'image_url')
    ordering = ['slug']  # 按照 'slug' 這個整數字段進行排序

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(User)
admin.site.register(BorrowRecord)
