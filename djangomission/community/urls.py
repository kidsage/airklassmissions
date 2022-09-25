from django.urls import path
from community.views import AnswerCreateView, QuestionCreateView, QuestionDetailVIew, QuestionListVIew

app_name = 'community'

urlpatterns = [   
    path('question/create/<int:pk>', QuestionCreateView.as_view(), name='question_create'),
    path('question/list', QuestionListVIew.as_view(), name='question_create'),
    path('question/detail/<int:pk>', QuestionDetailVIew.as_view(), name='question_detail'),
    path('answer/create/<int:pk>', AnswerCreateView.as_view(), name='question_create'),
]