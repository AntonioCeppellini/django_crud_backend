from .views import ArticleViewSet, UserViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

#####setting up our router#####
router = DefaultRouter()
router.register('articles', ArticleViewSet, basename = 'articles')
router.register('users', UserViewSet)


urlpatterns = [
    path('api/', include(router.urls)),#####api/before every route because is the name of our app

    #####using class based api views#####
    #path('articles/', ArticleList.as_view()),
    #path('articles/<int:id>/', ArticleDetails.as_view() )
    
    #####using functions based api views#####
    #path('articles', article_list),
    #path('articles/<int:pk>/', article_details)
]
