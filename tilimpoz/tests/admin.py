from django.contrib import admin
from .models import Answer, Question, TestModel, TestCategories

admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(TestModel)
admin.site.register(TestCategories)
