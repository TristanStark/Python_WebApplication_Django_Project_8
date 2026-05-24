from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ..models import Ticket, Review, UserFollows



@login_required
def feed(request):
    print("Feed page accessed")
    print(f"User: {request.user}")
    # Followed users and their posts
    following_users = UserFollows.objects.filter(user=request.user).values_list("followed_user", flat=True)

    following_tickets = Ticket.objects.filter(user__in=following_users).order_by("-time_created")
    following_reviews = Review.objects.filter(user__in=following_users).order_by("-time_created")

    # Your posts
    own_tickets = Ticket.objects.filter(user=request.user).order_by("-time_created")
    own_reviews = Review.objects.filter(user=request.user).order_by("-time_created")
    posts = sorted(
        list(own_tickets) + list(own_reviews) + list(following_tickets) + list(following_reviews),
        key=lambda x: x.time_created,
        reverse=True
    )

    return render(request, "feed.html", {"posts": posts})

