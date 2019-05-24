from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from .forms import HeroForm
from django.contrib import messages
from .models import Article, Hero

# Create your views here.


# for contact...

def contactFormHandle(request):
    received = 0
    if request.method == 'POST':
        received = 1
        print("Form Received")
        form = ContactForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'you have successfully submited your message')
        else:
            messages.error(
                request, 'Error submiting message. please enter correctly')
    context = {
        "form": ContactForm()
    }
    return context


# for hero...

@login_required(login_url='/admin/login')
def hero_create(request):

    received = 0
    if request.method == 'POST':
        received = 1
        print("Form Received")
        form = HeroForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'you have successfully submited your message')
        else:
            messages.error(
                request, 'Error submiting message. please enter correctly')
    context = {
        "form": HeroForm()
    }

    context = {
        "form": HeroForm()
    }
    return render(request, 'home/hero.html', context)


@login_required(login_url='/admin/login')
def hero_update(request, id=None):
    instance = get_object_or_404(Hero, id=id)
    form = HeroForm(request.POST or None,
                    request.FILES or None, instance=instance)
    if request.method == 'POST':
        received = 1
        print("Form Received")

        if form.is_valid():
            form.save()
            messages.success(
                request, 'you have successfully submited your message')
        else:
            messages.error(
                request, 'Error submiting message. please enter correctly')
    context = {
        "instance": instance,
        "form": form
    }
    return render(request, 'home/hero.html', context)


def index(request):
    article_list = Article.objects.all()
    hero_list = Hero.objects.all()
    print(article_list)
    context = {
        "hero_list": hero_list,
        "articles": article_list,
    }
    return render(request, 'home/index.html', context)


def story(request):
    story_list = Story.objects.all()
    context = {
        "story_list": story_list
    }


def story_detail(request, slug=None):
    instance = get_object_or_404(Story, slug=slug)
    context = {
        "instance": instance
    }
    return render(request, 'home/story-detail.html', context)


def story(request):
    context = {

    }
    return render(request, 'home/Story.html', context)


def contact(request):
    context = {

    }
    return render(request, 'home/contact.html', context)

    #  return HttpResponse("<h3 Hellow, i am done..../h3>")


def contact(request):
    context = {
        "form": contactFormHandle(request)

    }
    return render(request, 'home/contact.html', context)
