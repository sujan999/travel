from django.contrib import admin
from .models import Story, Tag


# Register your models here.

class StoryModelAdmin(admin.ModelAdmin):
    list_display = ["__str__","date", "title", "tag", "photographer", "draft"]
    list_dispay_links = ["__str__"]
    list_filter =["date", "tag", "photographer", "draft"]


    class Meta:
        model = Story


admin.site.register(Story, StoryModelAdmin)
admin.site.register(Tag)

