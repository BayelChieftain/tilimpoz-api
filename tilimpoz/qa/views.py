from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models.questions import Question
from .serializers.questions import ListQuestionSerializer, CreateQuestionSerializer


# Create your views here.


class QuestionListAPIView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = ListQuestionSerializer
    permission_classes = [AllowAny]


class QuestionCreateAPIView(CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = CreateQuestionSerializer
    permission_classes = [IsAuthenticated]
