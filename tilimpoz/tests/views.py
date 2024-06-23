from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .models.test_categories import TestCategories
from .models.questions import Question
from .models.tests import TestModel
from .serializers import TestCategorySerializer, TestModelSerializer, QuestionSerializer


# Create your views here.


class TestCategoryListAPIView(ListAPIView):
    queryset = TestCategories.objects.all()
    serializer_class = TestCategorySerializer


class TestListAPIView(ListAPIView):
    serializer_class = TestModelSerializer
    queryset = TestModel.objects.all()


class QuestionListAPIView(ListAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
