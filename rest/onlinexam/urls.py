from django.urls import path 
from .views import QuestionView,QuestionList,QuestionDetailView,QuestionUpdateView,ChoiceViewCreate

urlpatterns = [
    path('question/',QuestionView.as_view(),name = 'question'),
    path('questionlist/',QuestionList.as_view(),name = 'question-list'),
    path('questiondetail/<int:id>',QuestionDetailView.as_view(),name = 'question-detail'),
    path('questionupdate/<int:id>',QuestionUpdateView.as_view(),name = 'question-update'),
    path('choice/',ChoiceViewCreate.as_view(),name = 'choice'),
]