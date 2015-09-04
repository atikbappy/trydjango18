from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignUpForm, ContactForm

# Create your views here.


def index(request):
    title = "Welcome"

    # if request.user.is_authenticated():
    #     title = request.user.username

    # if request.method == "POST":
    #     print(request.POST)

    form = SignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)

        if not instance.full_name:
            instance.full_name = "Md Athikul Islam"

        instance.save()

        print(instance.full_name)
        print(instance.email)

    context = {"title": title, "form": form, }

    return render(request,"hello.html", context)



def contact(request):

    form = ContactForm(request.POST or None)

    if form.is_valid():
        print(form.cleaned_data)

    context = {"title": "Contact US", "form": form, }

    return render(request, "contact.html", context)