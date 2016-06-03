from django.conf.urls import url
from search import views

urlpatterns = [
    # 書籍
    url(r'^search_report/$', views.search_report, name='search_report'),   # 一覧
    # url(r'^report/add/$', views.report_edit, name='report_add'),  # 登録
    # url(r'^report/mod/(?P<report_id>\d+)/$', views.report_edit, name='report_mod'),  # 修正
    # url(r'^report/del/(?P<report_id>\d+)/$', views.report_del, name='report_del'),   # 削除
]