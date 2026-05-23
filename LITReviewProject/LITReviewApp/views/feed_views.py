from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib import messages

from ..forms import TicketForm
from ..models import Ticket, Review, UserFollows



@login_required
def feed(request):
    print("Feed page accessed")
    print(f"User: {request.user}")
    return render(request, "feed.html", {"posts": []})

