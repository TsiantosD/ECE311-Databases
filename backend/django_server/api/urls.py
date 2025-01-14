from django.urls import path
from . import views

urlpatterns = [
    path("post-by-id", views.post_by_id),
    path("posts-by-user", views.posts_by_user),
    path("user-by-id", views.user_by_id),
    path("react", views.react),
]