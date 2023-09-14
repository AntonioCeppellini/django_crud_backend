#####some of the import aren't used because where they are used is commented out, i tried to leave all the code or quite all the code to let understand quite every options#####
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Article
from .serializers import ArticleSerializer, UserSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework import status, generics, mixins, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


# Create your views here.
#####this is function base api views#####
""" @api_view(['GET', 'POST'])
def article_list(request):
    #get all articles
    if request.method == 'GET':
        articles =Article.objects.all()
        serializer = ArticleSerializer(articles, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def article_details(request, pk):
    try:
        article = Article.objects.get(pk = pk)
    
    except Article.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_404_NOT_FOUND404)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status = status.HTTP_204_NO_CONTENT) """

#####this is class based api views, using it with mixins help us to write more DRY code:D#####
#####seeing all the articles#####
"""
class ArticleList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    #####defining the queryset#####
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    #####get request to see all the articles#####
    def get(self, request):
        return self.list(request)
    #####post request to create a post#####
    def post(self, request):
        return self.create(request)

#####seeing a single article#####
class ArticleDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    #####defining the queryset#####
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    #####the lookup_field help us to locate the article we want to visualize#####
    lookup_field = 'id'
    #####get request to see a single article by its id#####   
    def get(self, request, id):
        return self.retrieve(request, id = id)
    #####put request to update a single article by its id#####
    def put(self, request, id):
        return self.update(request, id = id)
    #####delete request to delete a single article by its id#####
    def delete(self, request, id):
        return self.destroy(request, id = id) """

#####making views using viewsets#####
""" class ArticleViewSet(viewsets.ViewSet):
    #####getting all the articles#####
    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many = True)
        return Response(serializer.data)
    #####creating an article using viewsets#####
    def create(self, request):
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    #####retrieving a specific article#####
    def retrieve(self, request, pk = None):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, pk = pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    #####updating a specific article#####
    def update(self, request, pk = None):
        article = Article.objects.get(pk = pk)
        serializer = ArticleSerializer(article, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    #####deleting a specific article#####
    def destroy(self, request, pk = None):
        article = Article.objects.get(pk = pk)
        article.delete()
        return Response(status = status.HTTP_204_NO_CONTENT) """
        
#####using generic viewsets with mixin(superfast way)#####
""" class ArticleViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer """

#####using model viewset(fastest way! :D)#####
class ArticleViewSet(viewsets.ModelViewSet):
    #####setting the queryset#####
    #####a queryset is a collection of objects from the database#####
    queryset = Article.objects.all()
    #####serializer class used for validating input and serialize output#####
    #####(serializers are responsible for converting objects into data types understandable by JavaScript and front-end frameworks)#####
    serializer_class = ArticleSerializer
    #####authentication class, we want to specify what authentication we want#####
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication)

#####model viewset to create user#####
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer