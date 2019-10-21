from django.contrib import admin
from .models import Profile, Review, Project, Rate

admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Rate) 

