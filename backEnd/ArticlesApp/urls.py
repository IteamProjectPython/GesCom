from django.conf.urls import url
from django.urls import path
from ArticlesApp import views

urlpatterns = [
    url(r'^categories/$', views.categoriesApi),
    url(r'^categories/([0-9]+)$', views.categoriesApi),

    url(r'^articles/$', views.articlesApi),
    url(r'^articles/([0-9]+)$', views.articlesApi),
]

