from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib import messages

from ..forms import TicketForm
from ..models import Ticket, Review, UserFollows


@login_required
def review_create(request):
    return render(request, "review_form.html", {
        "review": None,
        "ticket": None,
    })


@login_required
def review_create_for_ticket(request, ticket_id):
    return render(request, "review_form.html", {
        "review": None,
        "ticket": None,
    })


@login_required
def review_edit(request, pk):
    return render(request, "review_form.html", {
        "review": None,
        "ticket": None,
    })


@login_required
def review_delete(request, pk):
    return redirect("posts")

