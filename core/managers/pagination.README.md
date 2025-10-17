📚 Paginate Query Helper for Django
This utility helps you paginate, search, filter, and order any Django queryset — with just one function call.

✅ Example: Using paginate_query in a Django API View
Below is a simple usage example for a Django API view using DRF (or any custom base view).

```
class SettingViews(BaseApiView):
    throttle_classes = ()
    permission_classes = ()

    @staticmethod
    def post(request, **kwargs):
        # Get pagination and sorting params from the request body
            page = request.data.get('page', 1)
            page_size = request.data.get('page_size', 10)
            search = request.data.get('search', None)
            orderby = request.data.get('orderby', None)
            order = request.data.get('order', None)

        # Example 1: Simple .values() query to select specific fields
        qs = Meter.objects.values(
            'id',
            'reference',
            'answer',
            'comment',
            'description',
            # Add any other Meter fields you need
        )

        # Example 2: Include related models with select_related and specific fields
        qs = Meter.objects.select_related(
            'equipment',
            'form',
            'parent_meter'
        ).values(
            'id',
            'reference',
            'answer',
            'equipment__id',
            'equipment__name',
            'form__id',
            'form__title',
            'parent_meter__id',
            'parent_meter__reference',
        )

        # Fields to search in
        search_fields = [
            'reference',
            'answer',
            'other_answer',
            'comment',
            'description',
        ]

        # Call the pagination helper
        result = paginate_query(
            qs,
            page=page,
            page_size=page_size,
            search=search,
            search_fields=search_fields,
            orderby=orderby,
            order=order,
        )

        return Response(result)

```


⚙️ How it works
Dynamic Search: Search across multiple fields with icontains.
Flexible Filtering: Add extra filters as needed.
Dynamic Ordering: Order by any field and direction.
Pagination: Uses Django’s Paginator under the hood.
Date Handling: Converts created and updated fields to strings if present.


🗂️ Example Request 
```
http://localhost:8000/api/v1/system/activities?page=1&page_size=1&search=&orderby=created&order=desc
```
Method: `GET`

✅ Example Response
```
{
  "data": [
    {
      "id": 1,
      "reference": "Meter-001",
      "answer": "42",
      "equipment__id": 3,
      "equipment__name": "Pump A"
    }
  ],
  "current_page": 1,
  "page_size": 10,
  "total_pages": 3,
  "total_records": 25,
  "has_next": true,
  "has_prev": false,
  "pages": [1, 2, 3]
}

```