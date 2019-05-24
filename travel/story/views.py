from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from .forms import StoryForm


from .models import Story, Tag


# Create your views here.


# for story{create & update}
@login_required(login_url='/admin/login')
def story_create(request):

    received = 0
    if request.method == 'POST':
        received = 1
        print("Form Received")
        form = StoryForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'you have successfully submited your message')
        else:
            messages.error(
                request, 'Error submiting message. please enter correctly')
    context = {
        "form": StoryForm()
    }

    context = {
        "form": StoryForm()
    }
    return render(request, 'home/story.html', context)


@login_required(login_url='/admin/login')
def story_update(request, id=None):
    instance = get_object_or_404(Story, id=id)
    form = StoryForm(request.POST or None,
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
    return render(request, 'home/story.html', context)


def story(request):
    story_list = Story.objects.all()
    tag_list = Tag.objects.all()
    context = {
        "story_list": story_list,
        "tag_list": tag_list,
    }
    return render(request, 'story/story.html', context)


def story_detail(request, slug=None):
    instance = get_object_or_404(Story, slug=slug)
    context = {
        "instance": instance
    }
    return render(request, 'story/story_detail.html', context)


def story_tag(request, name=None):
    story_list = Story.objects.filter(tag__name=name)
    tag_list = Tag.objects.all()

    context = {
        "story_list": story_list,
        "tag_list": tag_list,
        "name": name,
    }
    return render(request, 'story/tag-story.html', context)
