from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

def articles_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request,'articles/articles_list.html',{'articles': articles})

def article_details(request,slug):
    article = Article.objects.get(slug=slug)
    return render(request,'articles/article_details.html',{'article' : article})

@login_required(login_url="/accounts/login/")
def create_view(request):
    if request.method == 'POST':
        Newform = forms.CreateArticle(request.POST,request.FILES)
        if Newform.is_valid():
            # saving form to db
            instance = Newform.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('article:list')
    else:
        Newform = forms.CreateArticle()
    return render(request,'articles/create.html',{'form':Newform})
