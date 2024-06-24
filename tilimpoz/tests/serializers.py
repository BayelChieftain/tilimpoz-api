from rest_framework import serializers
from .models.test_categories import TestCategories
from .models.tests import TestModel
from .models.questions import Question
from .models.answers import Answer


class TestCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCategories
        fields = '__all__'


class TestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ('id', 'question', 'test', 'answers')

    def get_answers(self, obj):
        answer = Answer.objects.filter(
            question=obj,
        )
        if answer:
            return AnswerSerializer(answer, many=True).data
        else:
            return []
