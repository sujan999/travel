from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    #path('story/',views.story, name='story'),
    #path('story/<slug:slug>/',views.story_detail, name='storyDetail'),
    path('contact/', views.contact, name='contact'),

    path('hero/create', views.hero_create, name='hero_create'),
    path('hero/update/<int:id>', views.hero_update, name='hero_update'),

]
