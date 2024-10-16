from rest_framework import serializers
from .models import Question, Choice

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'choice_text', 'votes')

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, source='choice_set')
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date' ,'choices']

class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date']

        def validate_question_text(self, value):
            if 'spam' in value.lower():
                raise serializers.ValidationError("No spam allowed!")
            return value