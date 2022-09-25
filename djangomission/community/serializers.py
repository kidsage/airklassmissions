from rest_framework import serializers
from community.models import Question, Answer

#
class AnswerSerializer(serializers.ModelSerializer):
    writer = serializers.ReadOnlyField(source='writer.username')

    class Meta:
        model = Answer
        fields = ['writer', 'content']


class QuestionSerializer(serializers.ModelSerializer):
    writer = serializers.ReadOnlyField(source='writer.username')

    class Meta:
        model = Question
        fields = ['writer', 'content']


class QuestionListSerializer(serializers.ModelSerializer):
    answer = serializers.SerializerMethodField()
    writer = serializers.ReadOnlyField(source='writer.username')

    class Meta:
        model = Question
        fields = ['id', 'writer', 'content', 'answer']


    def get_answer(self, obj):
        queryset = Answer.objects.filter(question_id=obj.id)
        serializer = AnswerSerializer(queryset, many=True)

        return serializer.data


class QuestionDetailSerializer(serializers.ModelSerializer):
    answer = serializers.SerializerMethodField()
    writer = serializers.ReadOnlyField(source='writer.username')

    class Meta:
        model = Question
        fields = ['id', 'writer', 'content', 'answer']


    def get_answer(self, obj):
        queryset = Answer.objects.filter(question_id=obj.id)
        serializer = AnswerSerializer(queryset, many=True)

        return serializer.data