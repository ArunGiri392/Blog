from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="post-detail" ),

    path("read-later",views.ReadLaterview.as_view(), name="read-later")
]