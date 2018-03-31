from django.conf.urls import url
from . import views

app_name = 'article'

urlpatterns = [
    url(r'^$',views.articles_list, name='list'),
    url(r'^create/$',views.create_view,name='create'),
    url(r'^(?P<slug>[\w-]+)/$',views.article_details, name='detail')
]
