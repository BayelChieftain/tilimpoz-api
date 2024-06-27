from rest_framework import serializers

from ..models.questions import Question
from ..models.answers import Answer
from .answers import AnswerSerializer


class ListQuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ('nickname', 'question', 'created_at',  'answers')

    def get_answers(self, obj):
        answer = Answer.objects.filter(
            question=obj,
        )
        if answer:
            return AnswerSerializer(answer, many=True).data
        else:
            return []


class CreateQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('nickname', 'question')
