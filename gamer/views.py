from django.shortcuts import render

from .forms import AnswerForm, QuestionForm


def some_view(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            picked = form.cleaned_data.get("picked")
            print(picked)
    else:
        form = QuestionForm

    return render(request, "gamer/gameform.html", {"form": form})


def answer_view(request):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            print("Success")
    else:
        form = AnswerForm

    return render(request, "gamer/answerform.html", {"form": form})
