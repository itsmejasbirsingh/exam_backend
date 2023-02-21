from django.contrib import admin

# Register your models here.

from .models import Course, Question, Option, Testpaper, Difficulty, TestpaperAssign, TestpaperAttempt
admin.site.register(Course)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Testpaper)
admin.site.register(Difficulty)
admin.site.register(TestpaperAssign)
admin.site.register(TestpaperAttempt)
