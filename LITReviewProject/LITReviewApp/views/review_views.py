from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from ..forms import ReviewForm
from ..models import Review, Ticket


@login_required
def review_create(request):
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, "Review created successfully.")
            return redirect("posts")
        return render(
            request,
            "review_form.html",
            {
                "review": review_form,
                "ticket": None,
            },
        )

    return render(
        request,
        "review_form.html",
        {
            "review": None,
            "ticket": None,
        },
    )


@login_required
def review_create_for_ticket(request, ticket_id):
    if request.method == "POST":
        try:
            _ = Ticket.objects.get(id=ticket_id)
        except Ticket.DoesNotExist:
            messages.error(request, "Ticket does not exist.")

        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket_id = ticket_id
            review.save()
            messages.success(request, "Review created successfully.")
            return redirect("posts")
        return render(
            request,
            "review_form.html",
            {
                "review": review_form,
                "ticket": ticket_id,
            },
        )

    return render(
        request,
        "review_form.html",
        {
            "review": None,
            "ticket": None,
        },
    )


@login_required
def review_edit(request, pk):
    if request.method == "POST":
        try:
            review = Review.objects.get(id=pk, user=request.user)
        except Review.DoesNotExist:
            messages.error(request, "Review does not exist.")
            return redirect("posts")

        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            messages.success(request, "Review updated successfully.")
            return redirect("posts")
        return render(
            request,
            "review_form.html",
            {
                "review": review_form,
                "ticket": review.ticket_id,
            },
        )
    return render(
        request,
        "review_form.html",
        {
            "review": None,
            "ticket": None,
        },
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
