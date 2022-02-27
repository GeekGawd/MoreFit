from django.contrib import admin
from exercise.models import Category, VideoTutorials, Exercise, TextTutorials

# Register your models here.

class TextAdmin(admin.StackedInline):
    model = TextTutorials

class ExerciseAdmin(admin.ModelAdmin):
    inlines = [TextAdmin]

    class Meta:
        model = Exercise

class TextAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category)
admin.site.register(VideoTutorials)
admin.site.register(TextTutorials, TextAdmin)
admin.site.register(Exercise, ExerciseAdmin)