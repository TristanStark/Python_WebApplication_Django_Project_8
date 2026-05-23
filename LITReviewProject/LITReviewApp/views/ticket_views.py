from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages

from ..forms import TicketForm
from ..models import Ticket, Review, UserFollows




@login_required
def ticket_create(request):
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)

        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()

            messages.success(request, "Ticket créé avec succès.")
            return redirect("posts")

    else:
        form = TicketForm()

    return render(request, "ticket_form.html", {"form": form})    
    


@login_required
def ticket_edit(request, pk):
    return render(request, "ticket_form.html", {"ticket": None})


@login_required
def ticket_delete(request, pk):
    return redirect("posts")