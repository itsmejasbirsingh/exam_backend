from .filters import QuestionFilter
from .models import Course, Difficulty, Question, Option, Testpaper, TestpaperAssign, TestpaperAttempt
from .serializers import CourseSerializer, DifficultySerializer, OptionSerializer, QuestionReadSerializer, QuestionSerializer, TestpaperAssignQuestionsReadSerializer, TestpaperAssignReadSerializer, TestpaperAssignSerializer, TestpaperAttemptSerializer, TestpaperReadSerializer, TestpaperSerializer
from .pagination import DefaultPagination
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.db.models import Q, F, Sum, Case, Value


class CourseList(ListCreateAPIView):

    permission_classes = [IsAdminUser | IsAuthenticated]

    def get_queryset(self):
        return Course.objects.all()

    serializer_class = CourseSerializer

    pagination_class = DefaultPagination

    filter_backends = [SearchFilter]

    search_fields = ['title']


class CourseDetail(RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAdminUser]

    queryset = Course.objects.all()

    serializer_class = CourseSerializer


class DifficultyList(ListCreateAPIView):

    permission_classes = [IsAdminUser | IsAuthenticated]

    queryset = Difficulty.objects.all()

    serializer_class = DifficultySerializer


class QuestionList(ListCreateAPIView):

    permission_classes = [IsAdminUser]

    queryset = Question.objects.all()

    def get_serializer_class(self):
        if (self.request.method == 'GET'):
            return QuestionReadSerializer
        return QuestionSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter]

    filterset_class = QuestionFilter

    search_fields = ['title', 'description', 'option__option']


class QuestionDetail(RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAdminUser]

    queryset = Question.objects.all()

    serializer_class = QuestionSerializer


class OptionsList(ListCreateAPIView):

    permission_classes = [IsAdminUser]

    queryset = Option.objects.all()

    serializer_class = OptionSerializer


class TestPaperList(ListCreateAPIView):

    permission_classes = [IsAdminUser]

    queryset = Testpaper.objects.order_by('-id')

    def get_serializer_class(self):
        if (self.request.method == 'GET'):
            return TestpaperReadSerializer
        return TestpaperSerializer

    pagination_class = DefaultPagination


class TestPaperAssignList(ListCreateAPIView):

    permission_classes = [IsAdminUser | IsAuthenticated]

    def get_queryset(self):
        if (self.request.user.is_superuser):
            return TestpaperAssign.objects.all()
        return TestpaperAssign.objects.filter(user=self.request.user.pk)

    def get_serializer_class(self):
        if (self.request.method == 'GET'):
            return TestpaperAssignReadSerializer
        return TestpaperAssignSerializer

    pagination_class = DefaultPagination


class TestPaperAssignDetail(RetrieveAPIView):

    permission_classes = [IsAuthenticated]

    queryset = TestpaperAssign.objects.all()

    serializer_class = TestpaperAssignQuestionsReadSerializer

class TestpaperAttemptList(ListCreateAPIView):

    permission_classes = [IsAuthenticated]

    queryset = TestpaperAttempt.objects.all()

    serializer_class = TestpaperAttemptSerializer
