from django.conf.urls import url
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    #url(r'^$',views.index, name='index'),
    url(r'^$', TemplateView.as_view(template_name='index.html')),#name='home'),
    url(r'^image/$',views.image_list.as_view())
    #url(r'^image/(?P<image>(*.*?))$',views.image_detail.as_view())            # (?P<name>pattern) name: name of the group and pattern: pattern to match
]
