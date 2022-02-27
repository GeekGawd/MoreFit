from django.urls import path
from django.conf.urls import include
from .views import CreateExerciseView, ExerciseView

urlpatterns = [
    path('create-exercise/', CreateExerciseView.as_view(), name="create-exercise"),
    path('exercise/', ExerciseView.as_view(), name="exercise")
]