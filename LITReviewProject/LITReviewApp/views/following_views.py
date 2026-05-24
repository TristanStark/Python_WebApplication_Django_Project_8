from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from django.contrib import messages

from ..models import UserFollows



@login_required
def following(request):
    if (request.method == "POST"):
        username = request.POST.get("username")
        if username:
            try:
                followed_user = get_user_model().objects.get(username=username)
                UserFollows.objects.create(user=request.user, followed_user=followed_user)
                messages.success(request, f"You are now following {followed_user.username}.")
            except get_user_model().DoesNotExist:
                messages.error(request, "User does not exist.")
        else:
            messages.error(request, "No user selected to follow.")
        return redirect("following")
    
    following_relations = UserFollows.objects.filter(
        user=request.user
    ).select_related("followed_user")

    followers_relations = UserFollows.objects.filter(
        followed_user=request.user
    ).select_related("user")

    following = [relation.followed_user for relation in following_relations]
    followers = [relation.user for relation in followers_relations]
    print(f"Followers: {[f.username for f in followers]}")
    print(f"Following: {[f.username for f in following]}")
    return render(request, "following.html", {
        "following": following,
        "followers": followers,
    })

@login_required
def unfollow(request, user_id):
    print(f"Unfollow request for user_id: {user_id}")
    try:
        followed_user = get_user_model().objects.get(id=user_id)
        follow_relation = UserFollows.objects.filter(user=request.user, followed_user=followed_user)
        if follow_relation.exists():
            follow_relation.delete()
            messages.success(request, f"You have unfollowed {followed_user.username}.")
        else:
            messages.error(request, "You are not following this user.")
    except get_user_model().DoesNotExist:
        messages.error(request, "User does not exist.")
    return redirect("following")
