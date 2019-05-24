from django.urls import path

from . import views

app_name = 'story'

urlpatterns = [
    path('', views.story, name='story'),

    path('<slug:slug>/', views.story_detail, name='storyDetail'),
    path('tag/<str:name>/', views.story_tag, name='tagStory'),

    path('story/create', views.story_create, name='story_create'),
    path('story/update/<int:id>', views.story_update, name='story_update'),

]
