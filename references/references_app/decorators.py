from django.shortcuts import redirect

def admin_only(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login_view')  # Redirect to login page or unauthorized page
    return wrapper