from django.http import HttpResponse

from django.shortcuts import redirect


# we are going to create a decorator that will make login and register
#pages unavailable when user is logged in already


# decorator is a function that takes another function in as a parameter
# and let's add additional functionality before the original function is called
def unauthenticated_user(view_func):

    def wrapper_func(request,*args,**kwargs):
        #we are checking is user is authenicated
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request,*args,**kwargs)

    return wrapper_func

# Example of decorator

'''
@fucntion_A
Function_B(arguments):

function_A is performed before calling function B


There is a wrapper function in decorator that is executed first
and then the function that got the decorator is performed

'''

def allowed_users(allowed_roles=[]):
    def decorator(view_func):

        def wrapper_func(request,*args,**kwargs):
            # we are setting the variable to None
            group = None
            # we are checking if group exists for the user that is entering the system
            if request.user.groups.exists():
                # if it is - then it assigns the group name to the variable
                group = request.user.groups.all()[0].name
                # if the group of the user is in the group of allowed users
                if group in allowed_roles:
                    # then we are entering the page in a normal way
                    return view_func(request,*args,**kwargs)
                # if not - then HTTP response is generated with info that we are not allowed
                else:
                    return HttpResponse("You are not authorized to view this page")

        return wrapper_func
    return decorator


def admin_only(view_func):
    def wrapper_function(request,*args,**kwargs):
        group = None
        # we checked the user group
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        # if the user is customer then we are redirecting the user to user page
        # if it is admin - then we are executing the view_func
        if group == 'customer':
            return redirect('user_page')
        if group == 'admin':
            return view_func(request,*args,**kwargs)
    return wrapper_function