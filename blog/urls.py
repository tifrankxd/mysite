from django.urls import path, re_path
from . import views

from .views import post_detail, policy


urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    re_path(r"^nosotros/$", views.nosotros, name="nosotros"),
    path("policy/", policy, name="policy"),
    path("^(?P<slug>[-\w]+)/?(?!policy)$", post_detail, name="post_detail"),
]
