from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login , logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    return render( request, 'alog/reg.html' )


def signup(request):
    if request.method == 'POST':
        username = request.POST[ 'username' ]
        fname = request.POST[ 'fname' ]
        lname = request.POST[ 'lname' ]
        email = request.POST[ 'email' ]
        pass1 = request.POST[ 'pass1' ]
        pass2 = request.POST[ 'pass2' ]

        if len( username ) > 10:
            messages.error( request, 'Enter valid name.Your name should be within 10 character', extra_tags='alert' )
            return redirect( 'register' )
        if not username.isalnum():
            messages.error( request, 'Enter Valid Name.Your name should be in letter and numbers', extra_tags='alert' )
            return redirect( 'register' )

        if pass1 != pass2:
            if User.objects.filter( username=username ).exists():
                messages.error( request, 'Username Taken', extra_tags='alert' )
                return redirect( 'register' )
            elif User.objects.filter( email=email ).exists():
                messages.error( request, 'Email Taken', extra_tags='alert' )
                return redirect( 'register' )

            messages.error( request, 'Enter match password', extra_tags='alert' )
            return redirect( 'register' )

        if len( pass1 ) < 8:
            messages.error( request, 'Enter atleast eight character', extra_tags='alert' )
            return redirect( 'register' )

        else:
            user = User.objects.create_user( username=username, first_name=fname, email=email, password=pass1,
                                             last_name=lname )
        user.save();
        messages.success( request, "Your account is successfully created.", extra_tags='success' )
        return redirect( 'signup' )

    else:
        return render( request, 'alog/signup.html' )


def login1(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST[ 'loginpass' ]
        user = authenticate( username=loginusername, password=loginpass )
        if user is not None:
            login( request, user )
            messages.success( request, 'You are successfully logged in.')
            return redirect( 'login1' )
        else:
            messages.error( request,'Enter Valid Username ,please try again.')

            return redirect('login1' )
    else:
        return render( request, 'alog/login.html' )


def logout1(request):
        logout(request)
        messages.success( request, 'You are successfully logged out.' )
        return redirect( 'login1' )



