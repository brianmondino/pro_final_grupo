from .forms import UserLoginForm, UserSignUpForm,UserChangePassword,EditUserForm

def login_form(request):
    login_form = UserLoginForm()
    signup_form = UserSignUpForm()
    return {
        'loginForm': login_form,
        'signupForm': signup_form
    }

def changepassword(request):
    change_password = UserChangePassword()
    return {
        'changepassword': change_password
    }

def edituser_form(request):
    edituser_form = EditUserForm()
    return {
        'edituserform': edituser_form
    }