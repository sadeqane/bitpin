from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


def score_range(value):
    if value not in range(0, 6):
        raise ValidationError(_("Score should be between 0:5"))


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()


class Rate(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField(validators=[score_range])

    # class Meta:
    #     unique_together = ('owner', 'post')
