from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question


def index(request):
    """
    Show first 5 questions on home
    """

    data = Question.objects.order_by("-pub_date")

    # show on console joined list
    # questions = ", ".join(list(map(lambda q: q.question_text, data[:5])))
    # pritn(questions)

    context = {"questions": data[:5]}

    # Longer way to render
    # template = loader.get_template("polls/index.html")
    # return HttpResponse(template.render(context, request))

    return render(request, "polls/index.html", context)


def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")


def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
