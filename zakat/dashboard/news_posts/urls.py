from django.urls import path
from .views import *

app_name = 'news_posts'

urlpatterns = [
    path('newz/', NewsListView.as_view(), name='newz'),
    path('', NewsList.as_view(), name='news_list'),
    path('newz/create', NewsCreateView.as_view(), name='newz_create'),
    path('newz/<int:pk>/edit/', NewsEditView.as_view(), name='newz_edit'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
]
