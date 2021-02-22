from rest_framework import serializers
from .models import Question, Choice

class ChoiceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Choice
    fields = ['id', 'choice_text', 'votes']

    def create(self, validated_data):
      return Choice.objects.create(**validated_data)

# class QuestionListPageSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = Question
#     fields = ['id', 'question_text', 'pub_date', 'created_at', 'choices']

#     def create(self, validated_data):
#       return Question.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#       for key, value in validated_data.items():
#         setattr(instance, key, value)
#       instance.save()
#       return instance

class QuestionListPageSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    question_text = serializers.CharField(max_length=200)
    pub_date = serializers.DateTimeField()

    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

class QuestionDetailPageSerializer(QuestionListPageSerializer):
  choices = ChoiceSerializer(many=True, read_only=True)

class VoteSerializer(serializers.Serializer):
  choice_id = serializers.IntegerField()

class ChoiceSerializerWithVotes(ChoiceSerializer):
  votes = serializers.IntegerField(read_only=True)

class QuestionResultPageSerializer(QuestionListPageSerializer):
  choices = ChoiceSerializerWithVotes(many=True, read_only=True)
