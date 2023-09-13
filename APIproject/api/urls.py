from .views import article_list, article_details
from django.urls import path

urlpatterns = [
    path('articles', article_list),
    path('articles/<int:pk>/', article_details)
]
