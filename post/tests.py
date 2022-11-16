import random

from django.contrib.auth import get_user_model
from django.test import tag
from django.urls import reverse
from model_mommy import mommy
from rest_framework.exceptions import status
from rest_framework.test import APITestCase


class PostTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = mommy.make(get_user_model())
        cls.post = mommy.make("post.post")

    @tag("normal")
    def test_get_post_list(self):
        self.client.force_login(self.user)
        url = reverse("post-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class RateTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = mommy.make(get_user_model())
        cls.post = mommy.make("post.post")
        cls.rate = mommy.make("post.rate", owner=cls.user, post=cls.post)

    @tag("normal")
    def test_get_rate_list(self):
        self.client.force_login(self.user)
        url = reverse("rate")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @tag("normal")
    def test_create_rate_score(self):
        self.client.force_login(self.user)
        url = reverse("rate")
        data = {"post":self.post.pk, "score":random.randrange(0,5)}
        response = self.client.post(url,data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('score'), data.get("score"))


    @tag("normal")
    def test_create_rate_wrong_score(self):
        self.client.force_login(self.user)
        url = reverse("rate")
        data = {"post":self.post.pk, "score":10}
        response = self.client.post(url,data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
