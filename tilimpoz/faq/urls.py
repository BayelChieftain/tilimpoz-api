from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.FaqListAPIView.as_view(), name='faq'),
]

