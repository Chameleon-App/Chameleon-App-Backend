import json

from django.http import HttpResponse


class HealthCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == "/health":
            response = {"health": "ok", "api_v": "0.1"}
            return HttpResponse(json.dumps(response))
        return self.get_response(request)
