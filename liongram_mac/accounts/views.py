from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .forms import UserCreateForm


def signup_view(request):
    # GET 요청 시 html 응답
    if request.method == 'GET':
        form = UserCreateForm
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    else:
        pass
