from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import redirect, render

from ..forms import ReviewForm, TicketForm
from ..models import Review, Ticket


def _build_review_ticket_form(post_data=None, files_data=None):
    if post_data is None:
        return TicketForm()

    ticket_data = post_data.copy()
    ticket_data["title"] = post_data.get("ticket_title", "")
    ticket_data["description"] = post_data.get("ticket_description", "")

    ticket_files = None
    if files_data is not None:
        ticket_files = files_data.copy()
        if files_data.get("ticket_image") is not None:
            ticket_files["image"] = files_data["ticket_image"]

    return TicketForm(ticket_data, ticket_files)


def _render_review_form(
    request,
    *,
    review_form,
    ticket=None,
    ticket_form=None,
    is_editing=False,
):
    return render(
        request,
        "review_form.html",
        {
            "review_form": review_form,
            "ticket": ticket,
            "ticket_form": ticket_form,
            "is_editing": is_editing,
        },
    )


@login_required
def review_create(request):
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        ticket_form = _build_review_ticket_form(request.POST, request.FILES)
        if review_form.is_valid() and ticket_form.is_valid():
            with transaction.atomic():
                ticket = ticket_form.save(commit=False)
                ticket.user = request.user
                ticket.save()

                review = review_form.save(commit=False)
                review.user = request.user
                review.ticket = ticket
                review.save()

            messages.success(request, "Review created successfully.")
            return redirect("posts")

        return _render_review_form(
            request,
            review_form=review_form,
            ticket_form=ticket_form,
        )

    return _render_review_form(
        request,
        review_form=ReviewForm(),
        ticket_form=TicketForm(),
    )


@login_required
def review_create_for_ticket(request, ticket_id):
    try:
        ticket = Ticket.objects.get(id=ticket_id)
    except Ticket.DoesNotExist:
        messages.error(request, "Ticket does not exist.")
        return redirect("posts")

    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            messages.success(request, "Review created successfully.")
            return redirect("posts")

        return _render_review_form(
            request,
            review_form=review_form,
            ticket=ticket,
        )

    return _render_review_form(
        request,
        review_form=ReviewForm(),
        ticket=ticket,
    )


@login_required
def review_edit(request, pk):
    try:
        review = Review.objects.get(id=pk, user=request.user)
    except Review.DoesNotExist:
        messages.error(request, "Review does not exist.")
        return redirect("posts")

    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            messages.success(request, "Review updated successfully.")
            return redirect("posts")

        return _render_review_form(
            request,
            review_form=review_form,
            ticket=review.ticket,
            is_editing=True,
        )

    return _render_review_form(
        request,
        review_form=ReviewForm(instance=review),
        ticket=review.ticket,
        is_editing=True,
    )


@login_required
def review_delete(request, pk):
    if request.method == "POST":
        try:
            review = Review.objects.get(id=pk, user=request.user)
            review.delete()
            messages.success(request, "Review deleted successfully.")
        except Review.DoesNotExist:
            messages.error(request, "Review does not exist.")
    return redirect("posts")
