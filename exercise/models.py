from textwrap import indent
from unicodedata import category
from django.db import models
from django.forms import CharField

# Create your models here.

class Category(models.Model):
    categories = models.CharField(max_length=50)

    def __str__(self) -> str:
        return str(self.categories)

class Muscle(models.Model):
    type_of_muscle = models.CharField(max_length=75)
    category = models.ManyToManyField(Category)

    def __str__(self) -> str:
        return f"{self.type_of_muscle}"
    

class VideoTutorials(models.Model):
    video1 = models.URLField()
    video2 = models.URLField()

    def __str__(self) -> str:
        return str(self.video1)

class Exercise(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    muscle = models.ForeignKey(Muscle, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)    
    difficulty = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    video_tutorial = models.OneToOneField(VideoTutorials, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.category}->{self.title}"

class TextTutorials(models.Model):
    text = models.CharField(max_length=400)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.text}"


