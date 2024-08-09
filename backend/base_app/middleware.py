from django.shortcuts import redirect
from django.conf import settings


class RedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path not in  ['/register_user', '/login_user']:
            return redirect('register_user')
            
        response = self.get_response(request)
        return response