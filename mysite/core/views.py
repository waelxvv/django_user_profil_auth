from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from mysite.core.forms import SignUpForm


@login_required
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.DateDeNaissance = form.cleaned_data.get('DateDeNaissance')
            user.profile.Telephone = form.cleaned_data.get('Telephone')
            user.profile.Adresse = form.cleaned_data.get('Adresse')
            #user.profile.DateDeNaissance = form.cleaned_data.get('DateDeNaissance')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
