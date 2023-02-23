from distutils import dep_util
from rest_framework import serializers
from .models import Course, Difficulty, Question, Option, Testpaper, TestpaperAssign, TestpaperAttempt
from django.utils.text import slugify


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'slug']
        read_only_fields = ['slug']

    def create(self, validated_data):
        course = Course(**validated_data)
        course.slug = slugify(course.title)
        course.save()
        return course

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title')
        instance.slug = slugify(validated_data.get('title'))
        instance.save()
        return instance


class DifficultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Difficulty
        fields = ['id', 'title', 'slug']
        read_only_fields = ['slug']

    def create(self, validated_data):
        difficulty = Difficulty(**validated_data)
        difficulty.slug = slugify(difficulty.title)
        difficulty.save()
        return difficulty


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

    # def validate(self, data):
    #     if (
    #             data['option1'] != data['answer'] or
    #             data['option2'] != data['answer'] or
    #             data['option3'] != data['answer'] or
    #             data['option4'] != data['answer']):
    #         raise serializers.ValidationError(
    #             "Select a correct answer")
    #     return data

    def create(self, validated_data):
        question = Question(**validated_data)
        question.save()
        option = Option()
        request = self.context['request']
        option.option = request.data['option1']
        option.question = question
        option.answer = request.data['option1'] == request.data['answer']
        option.save()

        option = Option()
        option.option = request.data['option2']
        option.question = question
        option.answer = request.data['option2'] == request.data['answer']
        option.save()

        option = Option()
        option.option = request.data['option3']
        option.question = question
        option.answer = request.data['option3'] == request.data['answer']
        option.save()

        option = Option()
        option.option = request.data['option4']
        option.question = question
        option.answer = request.data['option4'] == request.data['answer']
        option.save()

        return question


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'option']


class QuestionReadSerializer(serializers.ModelSerializer):
    options = OptionSerializer(source='option_set', read_only=True, many=True)

    class Meta:
        model = Question
        fields = ['id', 'title', 'description', 'course',
                  'difficulty', 'options', 'correct_answer']
        depth = 1

    correct_answer = serializers.SerializerMethodField(
        method_name='get_correct_answer')

    def get_correct_answer(self, question: Question):
        option = Option.objects.filter(question=question, answer=True)
        return OptionSerializer(option.last()).data


class QuestionWithoutCorrectAnswerReadSerializer(serializers.ModelSerializer):
    options = OptionSerializer(source='option_set', read_only=True, many=True)

    class Meta:
        model = Question
        fields = ['id', 'title', 'description', 'course',
                  'difficulty', 'options']


class TestpaperSerializer(serializers.ModelSerializer):

    class Meta:
        model = Testpaper
        fields = ['id', 'title', 'description',
                  'time', 'question']

    def validate(self, data):
        if not data['question']:
            raise serializers.ValidationError("Add questions in test papers.")
        if (data['time'] < 10):
            raise serializers.ValidationError(
                "Time can not be less than 10 minutes.")
        elif (data['time'] > 120):
            raise serializers.ValidationError(
                "Time should not exeed 180 minutes.")
        return data


class TestpaperAssignSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestpaperAssign
        fields = '__all__'

    # Validate if testpaper is already assigned to selected users.
    def validate(self, data):
        assigned = TestpaperAssign.objects.filter(
            user__in=data['user']).filter(testpaper=data['testpaper']).last()
        if assigned is not None:
            userName = ''
            for user in assigned.user.all():
                userName += str(user) + ', '
            userName = userName[:-2]
            raise serializers.ValidationError(
                "Testpaper already assigned with %s" % (userName))
        return data


class TestpaperReadSerializer(serializers.ModelSerializer):
    assignment = TestpaperAssignSerializer(
        source='testpaperassign_set', read_only=True, many=True)

    question = QuestionWithoutCorrectAnswerReadSerializer(many=True)

    class Meta:
        model = Testpaper
        fields = ['id', 'title', 'description',
                  'time', 'question', 'assignment']


class TestpaperAssignQuestionsReadSerializer(serializers.ModelSerializer):
    testpaper = serializers.SerializerMethodField()

    class Meta:
        model = TestpaperAssign
        fields = ['id', 'start_at', 'end_at', 'testpaper']

    def get_testpaper(self, obj):
        return TestpaperReadSerializer(obj.testpaper).data


class TestpaperAttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestpaperAttempt
        fields = "__all__"
        read_only_fields = ['user', 'testpaperassign']


class TestpaperAssignReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestpaperAssign
        fields = ['id', 'start_at', 'end_at', 'testpaper', 'question_attempts_count']
        depth = 1

    question_attempts_count = serializers.SerializerMethodField(
        method_name='get_question_attempts_count')

    def get_question_attempts_count(self, obj):
        return TestpaperAttempt.objects.filter(user=self.context['request'].user).filter(testpaperassign=obj).count()
