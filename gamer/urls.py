from django.urls import path

from . import views

urlpatterns = [
    path('gamer/', views.some_view, name='some_view'),
    path('gamer_answers/', views.answer_view, name='answer_view')
]
