from unicodedata import category
from rest_framework import serializers
from .models import Exercise, TextTutorials
import json

class TextTutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextTutorials
        fields = ["text"]

class ExerciseSerializer(serializers.ModelSerializer):
    video_tutorials = serializers.SerializerMethodField()
    text_tutorials = TextTutorialSerializer(many=True, source="texttutorials_set")
    category = serializers.SerializerMethodField()
    muscle = serializers.SerializerMethodField()

    class Meta:
        model = Exercise
        fields = ["category", "muscle","title","difficulty","gender",
                "video_tutorials", "text_tutorials"]

    def get_video_tutorials(self, instance):
        qs = []
        qs.append(instance.video_tutorial.video1)
        qs.append(instance.video_tutorial.video2)
        return qs
    
    def get_category(self, instance):
        return str(instance.category.categories)
    
    def get_muscle(self, instance):
        return str(instance.muscle.type_of_muscle)