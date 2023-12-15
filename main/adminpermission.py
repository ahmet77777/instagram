from django.shortcuts import redirect 
def simple_middleware(get_response):
    def middleware(request):
        if not (request.path == "/" or '/adminbatyr/' in request.path or request.path == "/error/" or request.path == "/register/"):
            return redirect("/error/")

        response = get_response(request)
        return response
    return middleware