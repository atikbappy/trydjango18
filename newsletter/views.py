from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignUpForm

# Create your views here.


def index(request):
    title = "hi"

    if request.user.is_authenticated():
        title = request.user.username

    if request.method == "POST":
        print(request.POST)

    form = SignUpForm()

    context = {"title": title, "form": form, }

    return render(request,"hello.html", context)