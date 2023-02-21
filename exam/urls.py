from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.CourseList.as_view()),
    path('courses/<int:pk>/', views.CourseDetail.as_view()),
    path('difficulties/', views.DifficultyList.as_view()),
    path('questions/', views.QuestionList.as_view()),
    path('questions/<int:pk>/', views.QuestionDetail.as_view()),
    path('options/', views.OptionsList.as_view()),
    path('testpapers/', views.TestPaperList.as_view()),
    path('testpapers/assign/', views.TestPaperAssignList.as_view()),
    path('testpapers/assign/<int:pk>', views.TestPaperAssignDetail.as_view()),
    path('testpapers/attempt/<int:pk>', views.TestpaperAttemptList.as_view())
]