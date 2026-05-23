from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib import messages

from ..forms import TicketForm
from ..models import Ticket, Review, UserFollows



@login_required
def following(request):
    return render(request, "following.html", {
        "following": [],
        "followers": [],
    })



@login_required
def unfollow(request, user_id):
    return redirect("following")