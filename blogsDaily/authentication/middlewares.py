from django.shortcuts import redirect

def auth(view_function):
    def wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated == False:
            return redirect('authentication:signUp')
        return view_function(request, *args, **kwargs)
    return wrapped_view