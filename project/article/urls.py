from django.urls import path
from .views import *

app_name="user_info"
urlpatterns = [
    path('create/', ArticleCreateView.as_view(), name="article-create")
]
