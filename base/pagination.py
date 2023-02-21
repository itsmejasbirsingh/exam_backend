from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class DefaultPagination(PageNumberPagination):
    page_size = 20