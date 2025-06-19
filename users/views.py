from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import RegisterForm


# Create your views here.
def home(request):
    """Render the home page."""
    return render(request, "users/home.html")


def register(request):
    """Register a new user."""
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}")
            return redirect(to="/")
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {"form": form})
