from rest_framework.pagination import PageNumberPagination


class JourneyPaginator(PageNumberPagination):
    page_size = 10
