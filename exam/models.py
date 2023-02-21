from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

class Difficulty(models.Model):
    title = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField(blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    difficulty = models.ForeignKey(Difficulty, on_delete=models.PROTECT)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.CharField(max_length=256)
    answer = models.BooleanField(default=0)
    created_at = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.option

class Testpaper(models.Model):
    title = models.CharField(max_length=64, unique=True)
    description = models.TextField(null=True, blank=True)
    time = models.IntegerField(help_text="time in minutes", default=30)
    question = models.ManyToManyField(Question)

    def __str__(self):
        return self.title

class TestpaperAssign(models.Model):
    testpaper = models.ForeignKey(Testpaper, on_delete=models.CASCADE)
    user = models.ManyToManyField(User)
    start_at = models.DateTimeField(null=True)
    end_at = models.DateTimeField(null=True)

    def __str__(self):
        return "Testpaper: %s assigned to %s" % (self.testpaper, self.user.all())

class TestpaperAttempt(models.Model):
    testpaperassign = models.ForeignKey(TestpaperAssign, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    answer = models.ForeignKey(Option, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s attempted by %s with answer: %s" % (self.question, self.user, self.answer)