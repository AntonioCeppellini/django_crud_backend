from .views import ArticleList, ArticleDetails
from django.urls import path
#####using class based api views is better because it will be more browsable and the code will be more DRY#####
urlpatterns = [
    #####using class based api views#####
    path('articles/', ArticleList.as_view()),
    path('articles/<int:id>/', ArticleDetails.as_view() )
    
    #####using functions based api views#####
    #path('articles', article_list),
    #path('articles/<int:pk>/', article_details)
]
