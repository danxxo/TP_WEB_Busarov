from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new_questions(self):
        return self.order_by('-id')
    
    def hot_questions(self):
        return self.annotate(numLikes=models.Count('likes')).order_by('-numLikes')
    
    def tag_question(self, tag):
        return self.filter(tags__name=tag).order_by('-id')
    

class AnswerManager(models.Manager):
    def top_answers(self, question):
        return self.filter(question=question).annotate(
            isCorrectOrder=models.Case(
                models.When(isCorrect=True, then=models.Value(1)),
                default=models.Value(2),
                output_field=models.BooleanField(),
            )
        ).order_by('isCorrectOrder')

class ProfileManager(models.Manager):
    def best_members(self, num=7):
        return self.annotate(numAnswers=models.Count('answer')).order_by('-numAnswers')[:num]
    
class TagManager(models.Manager):
    def top_tags(self, num=10):
        return self.annotate(numQuestions=models.Count('questions')).order_by('-numQuestions')[:num]


class Profile(models.Model):
    profile = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    userAvatar = models.ImageField(default='upload/default/user.png')

    objects = ProfileManager()


class Tag(models.Model):
    name = models.CharField(max_length=30)

    objects = TagManager()

    def __str__(self) -> str:
        return f'{self.name}'


class Question(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    likes = models.ManyToManyField(Profile, 
                                   related_name='questions', 
                                   blank=True)
    tags = models.ManyToManyField(Tag, related_name='questions', blank=True)

    objects = QuestionManager()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f'Question: {self.pk}'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField()
    likes = models.ManyToManyField(Profile,
                                   related_name='answers',
                                   blank=True)
    isCorrect = models.BooleanField(default=False)

    objects = AnswerManager()

    def __str__(self):
        return f'Answer: {self.pk}'
    
    
