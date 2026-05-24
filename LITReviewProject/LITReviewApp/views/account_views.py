from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from ..forms import StyledPasswordChangeForm, UserProfileForm
from ..models import Review, Ticket, UserProfile


@login_required
def account(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)

    profile_form = UserProfileForm(instance=profile)
    password_form = StyledPasswordChangeForm(user=request.user)

    if request.method == "POST":
        action = request.POST.get("action")

        if action == "update_profile":
            profile_form = UserProfileForm(
                request.POST,
                request.FILES,
                instance=profile,
            )

            if profile_form.is_valid():
                updated_profile = profile_form.save(commit=False)

                if request.POST.get("remove_profile_picture") == "on":
                    updated_profile.profile_picture.delete(save=False)
                    updated_profile.profile_picture = None

                updated_profile.save()
                messages.success(request, "Profil mis à jour avec succès.")
                return redirect("account")

            messages.error(request, "Impossible de mettre à jour le profil.")

        elif action == "change_password":
            password_form = StyledPasswordChangeForm(
                user=request.user,
                data=request.POST,
            )

            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, "Mot de passe modifié avec succès.")
                return redirect("account")

            messages.error(request, "Impossible de modifier le mot de passe.")

    stats = {
        "ticket_count": Ticket.objects.filter(user=request.user).count(),
        "review_count": Review.objects.filter(user=request.user).count(),
        "following_count": request.user.following.count(),
        "followers_count": request.user.followed_by.count(),
    }

    return render(
        request,
        "account.html",
        {
            "profile": profile,
            "profile_form": profile_form,
            "password_form": password_form,
            "stats": stats,
        },
    )