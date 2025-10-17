from django.db import models
from datetime import datetime
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from core.managers.base import BaseManager


class PaginationManager(BaseManager):
    def paginate_query(self,
            queryset,
            *,
            page=1,
            page_size=10,
            search=None,
            search_fields=None,
            orderby=None,
            order=None,
            extra_filters=None,
    ):
        """
        Paginate a Django queryset with dynamic search, ordering, and filtering.

        Args:
            queryset: Django QuerySet.
            page (int): Page number.
            page_size (int): Items per page.
            search (str): Search keyword to filter fields in search_fields.
            search_fields (list): List of model fields for search (e.g., ['title', 'author__username']).
            orderby (str): Field to order by.
            order (str): 'asc' or 'desc'.
            extra_filters (dict): Additional exact filters to apply (e.g., {'status': 'active'}).

        Returns:
            dict with paginated data and metadata.
        """

        if extra_filters:
            queryset = queryset.filter(**extra_filters)

        if search and search_fields:
            q_obj = Q()
            for field in search_fields:
                q_obj |= Q(**{f"{field}__icontains": search})
            queryset = queryset.filter(q_obj)

        if orderby:
            order_prefix = '' if order.lower() == 'asc' else '-'
            queryset = queryset.order_by(f"{order_prefix}{orderby}")
        else:
            queryset = queryset.order_by('-id')

        total_count = queryset.count()
        paginator = Paginator(queryset, page_size)

        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        results = []
        for obj in page_obj.object_list:
            data = obj.copy()

            for dt_field in ['created', 'updated']:
                if dt_field in data and data[dt_field]:
                    dt_val = data[dt_field]
                    if isinstance(dt_val, datetime):
                        data[dt_field] = dt_val.strftime("%Y-%m-%d %H:%M:%S")

            data.pop('_state', None)
            results.append(data)

        return {
            "data": results,
            "current_page": page_obj.number,
            "page_size": page_size,
            "total_pages": paginator.num_pages,
            "total_records": total_count,
            "has_next": page_obj.has_next(),
            "has_prev": page_obj.has_previous(),
            "pages": list(range(1, paginator.num_pages + 1))
        }






