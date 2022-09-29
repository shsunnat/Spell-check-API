from django.shortcuts import render
from .serializers import SpellCheckSerializer
from .models import SpellCheck
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, CreateAPIView


class SpellCheckCreateAPI(CreateAPIView):
    queryset = SpellCheck.objects.all()
    serializer_class = SpellCheckSerializer


class SpellCheckRetrieveAPI(RetrieveAPIView):
    queryset = SpellCheck.objects.all()
    serializer_class = SpellCheckSerializer


def home(request):
    return render(request, 'home.html')

