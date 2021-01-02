from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ArticlesApp.serializers import CategoriesSerializer, ArticlesSerializer
from ArticlesApp.models import Categories, Articles

# Create your views here.

@csrf_exempt
def categoriesApi(request, id=0):
    if request.method == 'GET':
        categories = Categories.objects.all()
        categories_serializer = CategoriesSerializer(categories, many=True)
        return JsonResponse(categories_serializer.data, safe=False)
    
    elif request.method == 'POST':
        categories_data = JSONParser().parse(request)
        categories_serializer = CategoriesSerializer(data=categories_data)
        if categories_serializer.is_valid():
            categories_serializer.save()
            return JsonResponse('Données sauvegardés avec succès!!!', safe=False)
        return JsonResponse('Echec de la sauvegarde des données...', safe=False)
    
    elif request.method == 'PUT':
        categories_data = JSONParser().parse(request)
        categories = Categories.objects.get(IdCategorie=categories_data['IdCategorie'])
        categories_serializer = CategoriesSerializer(categories, data=categories_data)
        if categories_serializer.is_valid():
            categories_serializer.save()
            return JsonResponse('Modifications éffectuées avec succès!!!', safe=False)
        return JsonResponse('Echec de la modification des données...', safe=False)
    
    elif request.method == 'DELETE':
        categories_data = Categories.objects.get(IdCategorie = id)
        categories_data.delete()
        return JsonResponse('La supression a été effectuée avec succès!!!', safe=False)


@csrf_exempt
def articlesApi(request, id=0):
    if request.method == 'GET':
        articles = Articles.objects.all()
        articles_serializer = ArticlesSerializer(articles, many=True)
        return JsonResponse(articles_serializer.data, safe=False)

    elif request.method == 'POST':
        articles_data = JSONParser().parse(request)
        articles_serializer = ArticlesSerializer(data=articles_data)
        if articles_serializer.is_valid():
            articles_serializer.save()
            return JsonResponse('Données sauvegardés avec succès!!!', safe=False)
        return JsonResponse('Echec de la sauvegarde des données...', safe=False)
    
    elif request.method == 'PUT':
        articles_data = JSONParser().parse(request)
        articles = Articles.objects.get(IdArticle=articles_data['IdArticle'])
        articles_serializer = ArticlesSerializer(articles, data=articles_data)
        if articles_serializer.is_valid():
            articles_serializer.save()
            return JsonResponse('Modifications éffectuées avec succès!!!', safe=False)
        return JsonResponse('Echec de la modification des données...', safe=False)

    elif request.method == 'DELETE':
        articles_data = Articles.objects.get(IdArticle=id)
        articles_data.delete()
        return JsonResponse('La supression a été effectuée avec succès!!!', safe=False)