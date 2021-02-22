from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import json

from .models import Question, Choice
from .serializers import QuestionListPageSerializer, QuestionDetailPageSerializer, ChoiceSerializer, VoteSerializer, QuestionResultPageSerializer

# This decorator transforms our request object to become a DRF request and provides us with the argument 'data' that helps us get the body of the request
# The arguments passed into the decorator are HTTP methods accessible by this view

# route: 'questions/'
@api_view(['GET', 'POST'])
def questions_view(request):
  if request.method == 'GET':
    # Using the QuestionSerializer, we can modify this view to look neater
    questions = Question.objects.all()
    # To avoid issues when we decide to have relationships
    serializer = QuestionListPageSerializer(questions, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = QuestionListPageSerializer(data=request.data)
    if serializer.is_valid():
      Question.objects.create(**serializer.validated_data)
      resObject = {
        'message': 'Question created',
        'error': False
      }
      return Response(resObject, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# route: 'questions/<int:question_id>/'
@api_view(['GET', 'PATCH', 'DELETE'])
def question_detail_view(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  if request.method == 'GET':
    serializer = QuestionDetailPageSerializer(question)
    return Response(serializer.data)
  elif request.method == 'PATCH':
    serializer = QuestionDetailPageSerializer(question, data=request.data, partial=True)
    if serializer.is_valid():
      question = serializer.save()
      return Response(QuestionDetailPageSerializer(question).data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
    question.delete()
    resObject = {
      'message': 'Question deleted',
      'error': False
    }
    return Response(resObject, status=status.HTTP_200_OK)


@api_view(['POST'])
def choices_view(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  serializer = ChoiceSerializer(data=request.data)
  q = Question.objects.get(pk=question_id)
  choices = q.choice_set.all()
  length_of_choices = choices.count()
  if length_of_choices < 3:
    if serializer.is_valid():
      choice = serializer.save(question=question)
      return Response(ChoiceSerializer(choice).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  else:
    resObject = {
      'message': 'Enough choices for this question already',
      'error': True
    }
    return Response(resObject, status=status.HTTP_200_OK)


@api_view(['PATCH'])
def vote_view(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  serializer = VoteSerializer(data=request.data)
  if serializer.is_valid():
    choice = get_object_or_404(Choice, pk=serializer.validated_data['choice_id'], question=question)
    choice.votes += 1
    choice.save()
    resObject = {
      'message': 'Vote has been recorded',
      'error': False
    }
    return Response(resObject)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def question_result_view(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  serializer = QuestionResultPageSerializer(question)
  return Response(serializer.data)
