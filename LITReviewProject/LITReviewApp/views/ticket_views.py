from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from ..forms import TicketForm
from ..models import Ticket


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
    ticket = get_object_or_404(Ticket, pk=pk, user=request.user)

    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES, instance=ticket)

        if form.is_valid():
            form.save()
            messages.success(request, "Ticket modifié avec succès.")
            return redirect("posts")

    else:
        form = TicketForm(instance=ticket)

    return render(
        request,
        "ticket_form.html",
        {
            "form": form,
            "ticket": ticket,
        },
    )


@login_required
def ticket_delete(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk, user=request.user)
    ticket.delete()
    messages.success(request, "Ticket supprimé avec succès.")
    return redirect("posts")
