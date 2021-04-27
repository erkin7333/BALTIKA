from django.shortcuts import redirect



def anonymous_required(redirect_url):
      def _wrapped(view_func, *args, **kwargs):
          def check_anonymous(request, *args, **kwargs):
              if request.user.is_authenticated:
                  return redirect(redirect_url)
              view = view_func(request, *args, **kwargs)

              return view
          return check_anonymous
      return _wrapped