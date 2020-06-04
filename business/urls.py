from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(TemplateView\
        .as_view(template_name='business/businessHome.html')), \
        name='商家后台管理系统')
]