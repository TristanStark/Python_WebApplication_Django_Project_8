from django.contrib import admin
from .models import Ticket, UserFollows, Review

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "user",
        "time_created",
    )

    list_filter = (
        "time_created",
        "user",
    )

    search_fields = (
        "title",
        "description",
        "user__username",
    )

    readonly_fields = (
        "time_created",
    )


@admin.register(UserFollows)
class UserFollowsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "followed_user",
    )

    list_filter = (
        "user",
        "followed_user",
    )

    search_fields = (
        "user__username",
        "followed_user__username",
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "ticket",
        "user",
        "time_created",
    )

    list_filter = (
        "time_created",
        "ticket",
        "user",
    )

    search_fields = (
        "comment",
        "user__username",
    )

    readonly_fields = (
        "time_created",
    )

