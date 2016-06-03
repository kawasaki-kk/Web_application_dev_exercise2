from django.conf.urls import url
from accounts import views

# urlpatterns = [
#     # 書籍
#     url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}),
#     url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'accounts/logged_out.html'}),
# ]
urlpatterns = [
    # 書籍
    url(r'^login/$', views.login_view, name='login' ),
    url(r'^logout/$', views.logout_view, name='logout' ),
]