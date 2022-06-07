from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/new/', views.AddPost.as_view(), name='add_post'),
    path('<slug:slug>/update/', views.UpdatePost.as_view(), name='update_post'),
    path('<slug:slug>/delete/', views.DeletePost.as_view(), name='delete_post'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
]
