from .forms import LoginForm, SignupForm


def forms(request):
    context = {
        'login_form':LoginForm,
        'signup_form': SignupForm
    }
    return context
