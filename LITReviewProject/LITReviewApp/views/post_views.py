from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ..models import Ticket, Review

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
