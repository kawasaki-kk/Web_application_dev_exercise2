from django.conf.urls import url
from polls import views

urlpatterns = [
    # 書籍
    url(r'^report/$', views.report_list, name='report_list'),   # 一覧
    url(r'^report/add/$', views.report_edit, name='report_add'),  # 登録
    url(r'^report/mod/(?P<report_id>\d+)/$', views.report_edit, name='report_mod'),  # 修正
    url(r'^report/del/(?P<report_id>\d+)/$', views.report_del, name='report_del'),   # 削除
    # 感想
    url(r'^comment/(?P<report_id>\d+)/$', views.CommentList.as_view(), name='comment_list'),  # 一覧
    url(r'^comment/add/(?P<report_id>\d+)/$', views.comment_edit, name='comment_add'),        # 登録
    url(r'^comment/mod/(?P<report_id>\d+)/(?P<comment_id>\d+)/$', views.comment_edit, name='comment_mod'),  # 修正
    url(r'^comment/del/(?P<report_id>\d+)/(?P<comment_id>\d+)/$', views.comment_del, name='comment_del'),   # 削除
]