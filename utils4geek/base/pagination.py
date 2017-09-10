from rest_framework import pagination


class DefaultLimitOffsetPagination(pagination.PageNumberPagination):
    page_size = 20

    # max_page_size = 100

    def paginate_queryset(self, queryset, request, view=None):
        if request.GET.get("page", None) is None:
            return None
        return super(DefaultLimitOffsetPagination, self).paginate_queryset(queryset, request, view)


class PageNumberPagination(DefaultLimitOffsetPagination):
    page_size = 5