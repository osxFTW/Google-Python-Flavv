from django.utils.deprecation import MiddlewareMixin


class UsernameMiddleware(MiddlewareMixin):
    def process_template_response(self, request, response):
        if request.user.is_authenticated:
            response.context_data['username'] = request.user.username
        return response