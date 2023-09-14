from .views import ArticleViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

#####setting up our router#####
router = DefaultRouter()
router.register('articles', ArticleViewSet, basename = 'articles')

#####using class based api views is better because it will be more browsable and the code will be more DRY#####
urlpatterns = [
    path('', include(router.urls)),

    #####using class based api views#####
    #path('articles/', ArticleList.as_view()),
    #path('articles/<int:id>/', ArticleDetails.as_view() )
    
    #####using functions based api views#####
    #path('articles', article_list),
    #path('articles/<int:pk>/', article_details)
]
