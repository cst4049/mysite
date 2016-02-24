"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from myblog.views import ArticlePublishView,ArticleDetailView,ArticleEditView,RegisterView,GuestBookView,GuestBook_Form
from myblog.views import ArticleListView ,homepage,userinfo
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'index',ArticleListView.as_view(),name='blog_index'),
    url(r'article/publish$',ArticlePublishView.as_view(),name='blog_publish'),
    url(r'article/(?P<title>\w+\.?\w+)$',ArticleDetailView.as_view(),name='blog_detail'),
    url(r'article/(?P<title>\w+\.?\w+)/edit$',ArticleEditView.as_view(),name='blog_edit'),
    url(r'^$','myblog.views.homepage',name='blog_home'),
    url(r'^register/$',RegisterView.as_view(),name='register'),
    url(r'',include('django.contrib.auth.urls')),
    url(r'guestbook/$',GuestBookView.as_view(),name='blog_guestbook'),
    url(r'info/','myblog.views.userinfo',name='blog_userinfo'),
    url(r'guestbookform',GuestBook_Form.as_view(),name='guestbookform'),
    
    
]
