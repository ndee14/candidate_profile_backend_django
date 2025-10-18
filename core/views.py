from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from rest_framework import status
from rest_framework.views import APIView
from django.conf import settings




class HasAPIKey(BasePermission):
    """
    Permission class to check for a specific API key in headers
    """
    def has_permission(self, request, view):
        if settings.ENVIRONMENT != "prod":
            return True
        else:
            api_key = request.headers.get("x-api-key")
            expected_key = settings.MY_API_KEY
            return api_key == expected_key

class CacheMixin(object):
    cache_timeout = 60

    def get_cache_timeout(self):
        return self.cache_timeout

    def dispatch(self, *args, **kwargs):
        return cache_page(self.get_cache_timeout())(super(CacheMixin, self).dispatch)(*args, **kwargs)
    