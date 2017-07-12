from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

DEFAULT_PAGE_SIZE = 10
DEFAULT_MAX_PAGE_SIZE = 50


class BasePagination(PageNumberPagination):
    page_size = DEFAULT_PAGE_SIZE
    page_query_param = 'page_num'
    page_size_query_param = 'page_size'
    max_page_size = DEFAULT_MAX_PAGE_SIZE

    def get_paginated_response(self, data):
        page_size = self.page.paginator.per_page

        if len(data) < page_size:
            page_size = len(data)

        return Response({
            'total': self.page.paginator.count,
            'page_num': self.page.number,
            'page_size': page_size,
            'result': data,
        })
