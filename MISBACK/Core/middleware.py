# backend/core/middleware.py

from django.utils.deprecation import MiddlewareMixin

class CustomHeaderMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response['X-Custom-Header'] = 'My Custom Header'
        return response
