import imp
from random import randrange
import re
from tkinter import N
from django.shortcuts import render
from django.core.paginator import Paginator


QUESTIONS = [
    {
        'id': i,
        'title': f'Question {i}',
        'likes': randrange(1000),
        'content': f'Question {i} content. A lot of text, many many unknown info',
        'tags': [f'Tag1-{j}' for j in range(i, i+5)]
    } for i in range(1000)
]

def paginate(objects, request):
    page = request.GET.get('page')
    if page is None:
        page=1
    try:
        print(int(15.2))
        page = int(page)
    except ValueError:
        page = 1

    paginator = Paginator(objects, per_page=5)
    if page > paginator.num_pages:
        page = paginator.num_pages

    pg = paginator.page(page)
    print(pg.object_list)

    return paginator.page(page)

def index(request):
    return render(request,
                  'app/index.html',
                  {'questions': paginate(QUESTIONS, request)})

def question_detail(request, question_id):
    question = QUESTIONS[question_id]

    ANSWERS = [
    {
        'id': i,
        'content': f'Contents of Answer {i} from User. Really helpful answer ',
        'likes': randrange(200) 
    } for i in range(randrange(5))
]

    return render(
        request,
        'app/question_detail.html',
        {'question': question,
         'answers': ANSWERS}
    )

def user_settings(request):
    return render(
        request,
        'app/user_settings.html'
    )

def login(request):
    return render(
        request,
        'app/login.html'
    )

def signup(request):
    return render(
        request,
        'app/signup.html'
    )

def ask(request):
    return render(
        request,
        'app/ask.html'
    )

def tag(request, tag):
    return render(
        request,
        'tagged_list.html',
        {'tag': tag}
    )