from django.urls import path, include
from . import views

urlpatterns = [
    path('test-categories/', views.TestCategoryListAPIView.as_view(), name='test-categories-list'),
    path('tests/', views.TestListAPIView.as_view(), name='test-list'),
    path('questions/', views.QuestionListAPIView.as_view(), name='questions-list'),
]

