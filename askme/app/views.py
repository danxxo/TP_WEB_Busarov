from random import randrange
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Question, Answer, Tag, Profile


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

    return paginator.page(page)

def context_get(page=None, best_members=None, top_tags=None):
    return {'page': page, 'best_members': best_members, 'top_tags': top_tags}


def index(request):
    questions = Question.objects.new_questions()
    context = context_get(
        page=paginate(questions, request),
        best_members=Profile.objects.best_members(),
        top_tags=Tag.objects.top_tags()
    )
    return render(request,
                  'app/index.html',
                  context)


def hot(request):
    questions = Question.objects.hot_questions()
    context = context_get(
        page=paginate(questions, request),
        best_members=Profile.objects.best_members(),
        top_tags=Tag.objects.top_tags()
    )
    return render(request,
                'app/index.html',
                context)

def question_detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    answers = Answer.objects.top_answers(question_id)
    context = context_get(
        page=paginate(answers, request, per_page=5),
        best_members=Profile.objects.best_members(),
        top_tags=Tag.objects.top_tags()
    )
    context['question'] = question

    return render(
        request,
        'app/question_detail.html',
        context
        )

def user_settings(request):
    return render(
        request,
        'app/user_settings.html'
    )

def login(request):
    return render(
        request,
        'app/login.html',
    )

def signup(request):

    return render(
        request,
        'app/signup.html',
    )

def ask(request):
    return render(
        request,
        'app/ask.html',
    )

def tag(request, tag):
    questions = Question.objects.tag_question(tag)
    context = context_get(
        page=paginate(questions, request),
        best_members=Profile.objects.best_members(),
        top_tags=Tag.objects.top_tags()
    )
    context['tag'] = tag
    return render(
        request,
        'app/tagged_list.html',
        context
    )
