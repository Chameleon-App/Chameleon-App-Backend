import json

from django.http import HttpResponse
from apps.chameleon_api.repository.profile_repository import ProfileRepository


class HealthCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == "/health":
            response = {"health": "ok", "api_v": "0.1"}
            return HttpResponse(json.dumps(response))
        return self.get_response(request)


class CheckTokenMiddleware:
    repository = ProfileRepository()

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == "/api/auth/check_token":
            try:
                data = json.loads(request.body.decode(encoding="UTF-8"))
                token = data["token"]
            except:
                token = "null"
            response = {"isTokenAlive": self.repository.check_token(token)}
            return HttpResponse(json.dumps(response))
        return self.get_response(request)
