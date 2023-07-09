from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


def index(request):
    """
    Question index page - displays the latest few questions.
    """
    data = Question.objects.order_by("-pub_date")
    context = {"questions": data[:5]}
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    """
    Question detail page - displays a question text, with no results but with a form to vote.
    """
    return HttpResponse(f"You're looking at question {question_id}")


def results(request, question_id):
    """
    Question results page - displays results for a particular question.
    """
    return HttpResponse(f"You're looking at the results of question {question_id}")


def vote(request, question_id):
    """
    Vote action - handles voting for a particular choice in a particular question.
    """
    return HttpResponse(f"You're voting on question {question_id}")
