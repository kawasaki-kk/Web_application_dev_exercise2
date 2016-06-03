from django.contrib import admin


# Register your models here.
from polls.models import Report, Comment


class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publisher', 'date', 'content')  # 一覧に出したい項目
    list_display_links = ('id', 'title', 'content')  # 修正リンクでクリックできる項目
admin.site.register(Report, ReportAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment', 'commenter', 'date')
    list_display_links = ('id', 'comment',)
admin.site.register(Comment, CommentAdmin)