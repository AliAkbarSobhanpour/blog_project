from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article
# Create your views here.




class MainPageView(ListView):
    template_name = "blog/main.html"
    model = Article 



class ArticlePageView(DetailView):
    template_name = "blog/article-page.html"
    model = Article
    