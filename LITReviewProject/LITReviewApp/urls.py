# LITReviewApp/urls.py

from django.urls import path

from .views.auth_views import landing, logout, signup
from .views.feed_views import feed
from .views.following_views import following, unfollow
from .views.post_views import posts
from .views.review_views import (
    review_create,
    review_create_for_ticket,
    review_delete,
    review_edit,
)
from .views.ticket_views import (
    ticket_create,
    ticket_delete,
    ticket_edit,
)
from .views.account_views import account

urlpatterns = [
    path("", landing, name="landing"),
    path("signup/", signup, name="signup"),
    path("logout/", logout, name="logout"),

    path("feed/", feed, name="feed"),
    path("posts/", posts, name="posts"),
    path("following/", following, name="following"),

    path("account/", account, name="account"),
    
    path("tickets/create/", ticket_create, name="ticket_create"),
    path("tickets/<int:pk>/edit/", ticket_edit, name="ticket_edit"),
    path("tickets/<int:pk>/delete/", ticket_delete, name="ticket_delete"),

    path("reviews/create/", review_create, name="review_create"),
    path(
        "tickets/<int:ticket_id>/reviews/create/",
        review_create_for_ticket,
        name="review_create_for_ticket",
    ),
    path("reviews/<int:pk>/edit/", review_edit, name="review_edit"),
    path("reviews/<int:pk>/delete/", review_delete, name="review_delete"),

    path("following/<int:user_id>/unfollow/", unfollow, name="unfollow"),
]