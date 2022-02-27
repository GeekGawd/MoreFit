from unicodedata import category
from django.http import QueryDict
from rest_framework import generics, mixins
from rest_framework.response import Response
from exercise.models import Category, TextTutorials, VideoTutorials
from .serializers import ExerciseSerializer
from bs4 import BeautifulSoup as BSoup
import requests
from .models import Exercise, Muscle

# Create your views here.

class CreateExerciseView(generics.GenericAPIView, mixins.CreateModelMixin):

    def post(self, request):
        categories = ['Stretches', 'Bodyweight', 'Barbell', 'Dumbbells', 'Kettlebells']
        muscles = ['Traps', 'Shoulders', 'Chest', 'Biceps', 'Abdominals', 'Forearms', 'Quads'
                    'Calves', 'Triceps', 'Glutes', 'Traps_middle', 'Lats', 'Lowerback', 'Hamstrings']
        gender = ['Male']

        for i in gender:
            for j in categories:
                for k in muscles:
                    url = f"https://musclewiki.com/{j}/{i}/{k}"
                    print(url)
                    r = requests.get(url)
                    htmlcontent = r.content
                    soup = BSoup(htmlcontent, 'html.parser')
                    category, temp = Category.objects.get_or_create(categories=j)
                    muscle, temp4 = Muscle.objects.get_or_create(type_of_muscle=k)
                    titles = [exercise.text.strip() for exercise in soup.find_all("h3")]
                    data = soup.find_all("p")
                    links = list()
                    difficulty = list()

                    for temp1 in data:
                        for link in temp1.find_all('a'):
                            links.append(link.get('href'))

                    del links[0]
                    del links[-4: -1]
                    del links[-1]

                    videos = list()

                    for _ in range(0, len(links), 2):
                        video = VideoTutorials.objects.create(
                            video1=links[_],
                            video2=links[_+1]
                        )
                        videos.append(video)

                    for temp2 in data:
                        if temp2.findChildren('strong'):
                            difficulty.append(temp2.text)
                    
                    parse_steps = soup.select("ol.steps-list")

                    for num in range(len(titles)):
                        exercise = Exercise.objects.create(
                            category=category,
                            title=titles[num],
                            muscle=muscle,
                            gender=i,
                            difficulty=difficulty[num],
                            video_tutorial=videos[num]
                        )
                        
                        steps = [TextTutorials(
                            text=step.text,
                            exercise=exercise
                        ) for step in parse_steps[num] if step != '\n']

                        TextTutorials.objects.bulk_create(steps)
        return Response("Completed Successfully")

class ExerciseView(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ExerciseSerializer
    
    def get_queryset(self):
        muscle = Muscle.objects.get(type_of_muscle=self.request.data.get("muscle"))
        category = Category.objects.get(categories=self.request.data.get("category"))
        gender = self.request.data.get("gender")
        return Exercise.objects.filter(muscle=muscle).filter(category=category).filter(gender=gender)

    def post(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class GetAllExerciseView(generics.ListAPIView):
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()