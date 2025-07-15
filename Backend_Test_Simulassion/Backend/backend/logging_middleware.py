import time
from django.http import JsonResponse

class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # ✅ Allow OPTIONS method for CORS preflight
        if request.method == 'OPTIONS' or request.path.startswith('/shorturls/go/'):
            return self.get_response(request)

        start = time.time()

        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return JsonResponse({'error': 'Unauthorized'}, status=401)

        duration = round((time.time() - start) * 1000, 2)
        print(f"[LOG] {request.method} {request.path} - {duration}ms")
        return self.get_response(request)
