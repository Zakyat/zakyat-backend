from django.urls import path
from .views import *

app_name = 'news_posts'

urlpatterns = [
    path('', NewsList.as_view(), name='news_list'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
]
