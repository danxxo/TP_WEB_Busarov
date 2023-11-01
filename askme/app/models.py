from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    profile = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    userAvatar = models.ImageField(default='upload/default/user.png')



class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name


class Question(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    likes = models.ManyToManyField(Profile, 
                                   related_name='questions', 
                                   blank=True)
    tags = models.ManyToManyField(Tag, related_name='questions', blank=True)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField()
    likes = models.ManyToManyField(Profile,
                                   related_name='answers',
                                   blank=True)
    isCorrect = models.BooleanField(default=False)
