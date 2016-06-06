from django.conf.urls import url
from search import views

urlpatterns = [
    # 書籍
    url(r'^search_report/$', views.search_report, name='search_report'),   # 一覧
]