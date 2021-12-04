from django.urls import path
from . import views
from .feeds import LatestPostsFeed
from django.contrib.auth import views as auth_views


app_name = 'blog'

urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    path('about/', views.about, name='about'),    
    path('shop/', views.shop, name='shop'),
    # Django auth
    path('accounts/login', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('accounts/logout', auth_views.LogoutView.as_view(), name='logout'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    # path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('feed/', LatestPostsFeed(), name='post_feed'), 
    
]
