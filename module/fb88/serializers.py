from rest_framework import serializers

from module.fb88.models import Fb88, Question,Answer

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = '__all__'

class Fb88ListSerializers(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Fb88
        fields = ['id','name','question']
