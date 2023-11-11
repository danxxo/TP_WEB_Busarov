from typing import Any
from django.core.management import BaseCommand, CommandParser
from faker import Faker
from django.contrib.auth.models import User

from app.models import Question, Answer, Profile, User, Tag
import random

#fake = False()

class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument("ratio", type=int)

    def handle(self, *args, **kwargs):
        print('Started')
        ratio = kwargs['ratio']

        profiles = []
        users = []
        tags = []
        isCorrectChoices = [False] * 6 + [True]
        
        users = [
            User(username=f'user{i}',
                 password='pass') for i in range(ratio)
        ]
        User.objects.bulk_create(users)
        profiles = [
            Profile(profile=users[i]) for i in range(ratio)
        ]
        Profile.objects.bulk_create(profiles)
        print("PROFILES ADDED")

        tags = [
            Tag(name=f'tag_{i}') for i in range(ratio)
        ]
        Tag.objects.bulk_create(tags)
        print("TAGS ADDED")

        random_users = [
            random.choice(profiles) for i in range(ratio * 100)
        ]

        print('Start creating questions')

        questions = [
            Question(
                user=random_users[i],
                title=f'Question {i}',
                content=f'I need to know how to spell {i}. such a hard number',
            ) for i in range(ratio * 10)
        ]
        Question.objects.bulk_create(questions)
        print('------------------------')
        random_tags = [
            [random.choice(tags) for _ in range(4)] for _ in range(ratio * 10)
        ]
        print(len(random_tags), len(random_tags[0]))

        random_likes = [
            [random.choice(profiles) for _ in range(random.randrange(0, ratio))] for _ in range(ratio * 10)
        ]

        print('questions tagging and liking')
        for i in range(ratio * 10):
            print(i, 'of', ratio*10)
            questions[i].tags.set(random_tags[i])
            questions[i].likes.set(random_likes[i])

            answers = [
                Answer(
                    question=questions[i],
                    user=profiles[j],
                    content=f'Answer on Question{i} by number {j}',
                    isCorrect=random.choice(isCorrectChoices)
                ) for j in range(10)
            ]
            Answer.objects.bulk_create(answers)
            for j in range(len(answers)):
                answers[j].likes.set(random_likes[j])

        

        


