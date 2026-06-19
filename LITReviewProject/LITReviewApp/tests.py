from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Review, Ticket, UserFollows


class FollowingViewTests(TestCase):
    def setUp(self):
        self.user_model = get_user_model()
        self.follower = self.user_model.objects.create_user(
            username="alice",
            password="testpass123",
        )
        self.followed = self.user_model.objects.create_user(
            username="bob",
            password="testpass123",
        )
        self.client.force_login(self.follower)

    def test_duplicate_follow_does_not_create_server_error(self):
        UserFollows.objects.create(user=self.follower, followed_user=self.followed)

        response = self.client.post(
            reverse("following"),
            {"username": self.followed.username},
        )

        self.assertRedirects(response, reverse("following"))
        self.assertEqual(
            UserFollows.objects.filter(
                user=self.follower,
                followed_user=self.followed,
            ).count(),
            1,
        )


class ReviewViewTests(TestCase):
    def setUp(self):
        self.user_model = get_user_model()
        self.user = self.user_model.objects.create_user(
            username="reader",
            password="testpass123",
        )
        self.client.force_login(self.user)

    def test_review_create_builds_ticket_and_review(self):
        response = self.client.post(
            reverse("review_create"),
            {
                "ticket_title": "A valid title",
                "ticket_description": (
                    "A distinct description for the requested review."
                ),
                "headline": "Worth reading",
                "body": "A concise review body.",
                "rating": 4,
            },
        )

        self.assertRedirects(response, reverse("posts"))
        self.assertEqual(Ticket.objects.count(), 1)
        self.assertEqual(Review.objects.count(), 1)
        review = Review.objects.select_related("ticket").get()
        self.assertEqual(review.user, self.user)
        self.assertEqual(review.ticket.user, self.user)
        self.assertEqual(review.ticket.title, "A valid title")

    def test_review_create_for_missing_ticket_redirects_without_creating_review(self):
        response = self.client.post(
            reverse("review_create_for_ticket", args=[999999]),
            {
                "headline": "Still valid",
                "body": "This should not be saved.",
                "rating": 5,
            },
        )

        self.assertRedirects(response, reverse("posts"))
        self.assertEqual(Review.objects.count(), 0)
