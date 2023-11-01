from random import randrange
from django.shortcuts import render


QUESTIONS = [
    {
        'id': i,
        'title': f'Question {i}',
        'likes': randrange(1000),
        'content': f'Question {i} content. A lot of text, many many unknown info',
        'tags': [f'Tag1-{j}' for j in range(i, i+5)]
    } for i in range(10)
]

def index(request):
    return render(request,
                  'app/index.html',
                  {'questions': QUESTIONS})

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