from django.urls import path
from .views import MainPageView, ArticlePageView


urlpatterns = [
    path("", MainPageView.as_view(), name="main-page"),
    path("<pk>", ArticlePageView.as_view(), name="article-page")
]
