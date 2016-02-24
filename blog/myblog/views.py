#coding:utf-8
from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import F
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from forms import ArticlePublishForm,RegisterForm,GuestBookForm
from models import *
from django.http import Http404
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse,reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required
#from django.contrib.auth import authenticate,login
from django.contrib.auth import *

class RegisterView(FormView):
    template_name='registration/blog_register.html'
    form_class=RegisterForm
    success_url=reverse_lazy('blog_index')
    def form_valid(self,form):
        form.save()
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super(RegisterView, self).form_valid(form)


def homepage(request):
    return render(request,'blog_home.html')
def userinfo(request):
    return render(request,'blog_userinfo.html')
class AdminRequiredMixin(object):
    @classmethod
    def as_view(cls,**initkwargs):
        view=super(AdminRequiredMixin,cls).as_view(**initkwargs)
        return staff_member_required(view)

class ArticlePublishView(AdminRequiredMixin, FormView):
    template_name='blog_publish.html'
    form_class=ArticlePublishForm
    success_url='/index/'
    
    def form_valid(self,form):
        form.save(self.request.user.username)
        return super(ArticlePublishView,self).form_valid(form)

class ArticleListView(ListView):
    template_name='blog_index.html'
    def get_queryset(self,**kwargs):
        object_list=Article.objects.all().order_by(F('created'))[:100]
        paginator=Paginator(object_list,5)
        page=self.request.GET.get('page')
        try:
            object_list=paginator.page(page)
        except PageNotAnInteger:
            object_list=paginator.page(1)
        except EmptyPage:
            object_list=paginator.page(paginator.num_pages)
        return object_list 

class ArticleDetailView(DetailView):
    template_name='blog_detail.html'
    def get_object(self,**kwargs):
        title=self.kwargs.get('title')
        try:
            article=Article.objects.get(title=title)
            article.views+=1
            article.save()
            article.tags=article.tags.split()
        except Article.DoesNotExist:
            raise Http404("Article does not exist")
        return article    
         
class ArticleEditView(AdminRequiredMixin,FormView):
    template_name='blog_publish.html'
    form_class=ArticlePublishForm
    article=None
    def get_initial(self,**kwargs):
        title=self.kwargs.get('title')
        try:
            self.article=Article.objects.get(title=title)
            initial={
            'title':title,
            'content':self.article.content,
            'tags':self.article.tags,
            }
            return initial
        except Article.DoesNotExist:
            raise Http404("Article does not exist")
    def form_valid(self,form):
        form.save(self.request,self.article)
        return super(ArticleEditView,self).form_valid(form)
    def get_success_url(self):
        title=self.request.POST.get('title')
        success_url=reverse('blog_detail',args=(title,))
        return success_url
class GuestBookView(ListView):
    template_name='blog_guestbook.html'
    form_class=GuestBookForm
    
    def get_queryset(self,**kwargs):
        object_list=GuestBook.objects.all().order_by(F('created').desc())[:100]
        return object_list
class GuestBook_Form(FormView):
    template_name='blog_guestbookform.html'
    form_class=GuestBookForm
    success_url='/guestbook/'
    def form_valid(self,form):
        form.save(self.request.user.username)
        return super(GuestBook_Form,self).form_valid(form)   