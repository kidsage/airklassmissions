from django.urls import path, include
from contentshub.views import CommentCreateView, CommentDetailView, KlassCreateView, KlassDetailView, KlassListView

app_name = 'contentshub'

urlpatterns = [
    path('klass/list', KlassListView.as_view(), name='klass_list'),
    path('klass/create', KlassCreateView.as_view(), name='klass_create'),
    path('klass/detail/<int:pk>', KlassDetailView.as_view(), name='klass_detail'),
    path('comment/create/<int:pk>', CommentCreateView.as_view(), name='comment_create'),
    path('comment/detail/<int:pk>', CommentDetailView.as_view(), name='comment_detail'),
]