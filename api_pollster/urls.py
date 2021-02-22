from .apiviews import questions_view, question_detail_view, choices_view, vote_view, question_result_view
from django.urls import path

urlpatterns = [
  path('questions/', questions_view, name='questions_view'),
  path('questions/<int:question_id>/', question_detail_view, name='question_detail_view'),
  path('questions/<int:question_id>/choices/', choices_view, name='choices_view'),
  path('questions/<int:question_id>/vote/', vote_view, name='vote_view'),
  path('questions/<int:question_id>/result/', question_result_view, name='question_result_view')
]
