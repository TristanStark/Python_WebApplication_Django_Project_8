from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
)
from django.contrib.auth import (
    logout as auth_logout,
)
from django.shortcuts import redirect, render


def landing(request):
    print("Landing page accessed")
    print(f"User: {request.user}")
    print(f"Is authenticated: {request.user.is_authenticated}")
    print(f"Username: {request.user.username}")
    print(f"Data: {request.data if hasattr(request, 'data') else 'N/A'}")
    print(f"Post data: {request.POST if request.method == 'POST' else 'N/A'}")
    print(f"Request method: {request.method}")
    print(f"Request path: {request.path}")
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("feed")
        return render(request, "landing.html")
    if request.method == "POST":
        # Login logic
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(f"Attempting login with username: {username}")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("feed")
        else:
            print("Login failed")
    return render(request, "landing.html")


def signup(request):
    print("Signup page accessed")
    print(f"User: {request.user}")
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("feed")
        return render(request, "signup.html")
    if request.method == "POST":
        # Signup logic
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        print(f"Attempting signup with username: {username}")
        if not username or not password1 or not password2:
            print("All fields are required")
            return render(request, "signup.html", {"error": "All fields are required"})
        if password1 != password2:
            print("Passwords do not match")
            return render(request, "signup.html", {"error": "Passwords do not match"})
        if get_user_model().objects.filter(username=username).exists():
            print("Username already exists")
            return render(request, "signup.html", {"error": "Username already exists"})
        user = get_user_model().objects.create_user(
            username=username, password=password1
        )
        login(request, user)
        return redirect("feed")


def logout(request):
    auth_logout(request)
    return redirect("landing")
