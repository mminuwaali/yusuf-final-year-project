from django.shortcuts import redirect


def role_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser or request.user.is_staff:
                return redirect("admin:index")
            else:
                return redirect("account:index-view")

        return function(request, *args, **kwargs)

    return wrap
