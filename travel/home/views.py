from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Article, Hero, Story 

# Create your views here.

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
