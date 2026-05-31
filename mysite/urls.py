from django.contrib import admin
from django.urls import path
from blog.views import (
    home,
    posts_list,
    create_post,
    post_detail,
    edit_post,
    delete_post
)
from blog.views import (
    home, posts_list, create_post, post_detail,
    edit_post, delete_post,
    api_posts, api_post_detail, api_comments, api_categories
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home
    path('', home),

    # Posts
    path('posts/', posts_list),
    path('posts/create/', create_post),
    path('posts/<int:id>/', post_detail),
    path('posts/<int:id>/edit/', edit_post),
    path('posts/<int:id>/delete/', delete_post),
    # Auth
    path('login/', auth_views.LoginView.as_view(template_name='login.html')),
    path('logout/', auth_views.LogoutView.as_view(next_page='/')),
    path('api/posts/', api_posts),
    path('api/posts/<int:id>/', api_post_detail),
    path('api/posts/<int:id>/comments/', api_comments),
    path('api/categories/', api_categories),
]
