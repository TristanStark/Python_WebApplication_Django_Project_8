from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib import messages

from ..forms import TicketForm
from ..models import Ticket, Review, UserFollows



@login_required
def posts(request):
    # Your posts
    tickets = Ticket.objects.filter(user=request.user).order_by("-time_created")
    reviews = Review.objects.filter(user=request.user).order_by("-time_created")
    posts = sorted(
        list(tickets) + list(reviews),
        key=lambda x: x.time_created,
        reverse=True
    )
    return render(request, "posts.html", {"posts": posts})
