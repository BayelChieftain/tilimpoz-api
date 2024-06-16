from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from .models import Faq
from .serializers import FaqSerializer


# Create your views here.


class FaqListAPIView(ListAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer
    permission_classes = [AllowAny]