from django.urls import path
from . import views
from .views import (PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentCreateView, 
                    CommentUpdateView, ReplyCreateView, ReplyUpdateView)


urlpatterns = [
    path('', PostListView.as_view(), name ="home"),
    path('post/<int:pk>/', PostDetailView.as_view(), name ="postDetail"),
    path('post/new/', PostCreateView.as_view(), name ="postCreate"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name ="postUpdate"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name ="postDelete"),
    path('post/<int:pk>/comment/', CommentCreateView.as_view(), name ="addComment"),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name ="updateComment"),
    path('comment/<int:pk>/reply/', ReplyCreateView.as_view(), name ="addReply"),
    path('reply/<int:pk>/update/', ReplyUpdateView.as_view(), name ="updateReply"),
]