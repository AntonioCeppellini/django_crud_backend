from django.shortcuts import render, HttpResponse
from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework import status

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

#####this is class based api views#####
#####seeing all the articles#####
class ArticleList(APIView):
    #####get request to see all the articles#####
    def get(self, resquest):
        articles =Article.objects.all()
        serializer = ArticleSerializer(articles, many = True)
        return Response(serializer.data)
    #####post request to create a post#####
    def post(self, request):
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#####seeing a single article#####
class ArticleDetails(APIView):
    #####get a single article by its id#####
    def get_object(self, id):
        try:
            return Article.objects.get(id = id)
    
        except Article.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
    #####get request to see a single article by its id#####   
    def get(self, request, id):
        article = self.get_object(id = id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    #####put request to update a single article by its id#####
    def put(self, request, id):
        article = self.get_object(id = id)
        serializer = ArticleSerializer(article, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_404_NOT_FOUND404)
    #####delete request to delete a single article by its id#####
    def delete(self, request, id):
        article = self.get_object(id = id)
        article.delete()
        return Response(status = status.HTTP_204_NO_CONTENT) 
