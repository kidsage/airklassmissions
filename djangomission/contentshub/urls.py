from django.urls import path, include
from contentshub.views import KlassCreateView, KlassDetailView, KlassListView

app_name = 'contentshub'

urlpatterns = [
    path('list', KlassListView.as_view(), name='list'),
    path('create', KlassCreateView.as_view(), name='create'),
    path('detail/<int:pk>', KlassDetailView.as_view(), name='detail'),
]