from django.contrib import admin
from myblog.models import Post, Category

class CategoryAdmin(admin.ModelAdmin):
    pass

class CategoryInlineAdmin(admin.TabularInline):
    model = Category.posts.through
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts', )

class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInlineAdmin, ]

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)