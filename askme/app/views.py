from random import randrange
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Question, Answer, Tag, Profile


QUESTIONS = [
    {
        'id': i,
        'title': f'Question {i}',
        'likes': randrange(1000),
        'content': f'Question {i} content. A lot of text, many many unknown info',
        'tags': [f'Tag1-{j}' for j in range(i, i+5)]
    } for i in range(1000)
]

def paginate(objects, request, per_page=5):
    page = request.GET.get('page')

    try:
        page = int(page)
    except:
        page = 1

    if page <= 0:
        page = 1

    paginator = Paginator(objects, per_page)
    if page > paginator.num_pages:
        page = paginator.num_pages

    pg = paginator.page(page)
    print(pg.object_list)

    return paginator.page(page)

def index(request):
    questions = Question.objects.all()
    return render(request,
                  'app/index.html',
                  {'page': paginate(questions, request)})


def hot(request):
    return render(request,
                'app/index.html',
                {'page': paginate(QUESTIONS, request)})

def question_detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    answers = Answer.objects.filter(question=question)

    ANSWERS = [
    {
        'id': i,
        'content': f'Contents of Answer {i} from User. Really helpful answer ',
        'likes': randrange(200) 
    } for i in range(10)
]

    return render(
        request,
        'app/question_detail.html',
        {'question': question,
         'page': paginate(answers, request, per_page=3)}
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
        'app/tagged_list.html',
        {'tag': tag,
         'page': paginate(QUESTIONS, request)}
    )
