from django.contrib import admin
from .models import Assessment, Question, Option, Response

admin.site.register(Assessment)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Response)
