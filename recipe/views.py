from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from recipe.models import Recipe
from recipe.serializers import RecipeSerializer


class RecipesView(APIView):

    def get(self, *args, **kwargs):
        recipes = Recipe.objects.all()
        return Response(RecipeSerializer(recipes, many=True).data)

