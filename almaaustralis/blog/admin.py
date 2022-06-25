from django.contrib import admin
from .models import Tema, Post, PostComment
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class TemaResourse(resources.ModelResource):
    class Meta:
        model = Tema

class PostResourse(resources.ModelResource):
    class Meta:
        model = Post

class PostCommentResourse(resources.ModelResource):
    class Meta:
        model = PostComment

class TemaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    resource_class = TemaResourse

class PostAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ['title', 'author', 'post_tema','published']
    search_fields = ('title', 'author__username', 'tema__name')
    ordering = ('published', 'author')
    date_hierarchy = 'published'
    list_filter = ('author__username', 'tema__name')
    resource_class = PostResourse

    def post_tema(self, obj):
        return ",".join([c.name for c in obj.tema.all().order_by("name")])
    post_tema.short_description = "Temas"

class PostCommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'user', 'content', 'active']
    ordering = ('created',)
    search_fields = ('post',)
    resource_class = PostComment

admin.site.register(Tema, TemaAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostComment, PostCommentAdmin)