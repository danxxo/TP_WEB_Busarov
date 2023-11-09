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
        ratio = kwargs['ratio']

        profiles = []
        tags = []
        
        for i in range(ratio):
            new_user = User.objects.create_user(username=f'user{i}')
            new_user.set_password('pass')
            new_user.save()

            new_profile = Profile.objects.create(profile=new_user)
            new_profile.save()
            profiles.append(new_profile)

            new_tag = Tag.objects.create(name=f'Tag_{i}')
            new_tag.save()
            tags.append(new_tag)

        for i in range(ratio * 10):
            user = random.choice(profiles)
            title = f'Question'
            content = f'I need to know how to spell {i}. such a hard number'
            question_tags = []
            for j in range(10):
                tag = random.choice(tags)
                if tag not in question_tags:
                    question_tags.append(tag)

            new_question = Question.objects.create(
                user=user,
                title=title,
                content=content,
            )
            new_question.tags.set(question_tags)
            new_question.save()
            for _ in range(10):
                user = random.choice(profiles)
                new_answer = Answer.objects.create(
                    question=new_question,
                    user=user,
                    content=f'That is simple to spell {i}. Answer by {user}',
                    isCorrect=random.choice([True, False])
                )
                new_answer.save()


