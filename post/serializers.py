from django.db.models import Avg
from rest_framework import serializers

from post.models import Post, Rate


class PostSerializer(serializers.ModelSerializer):
    count_of_rates = serializers.SerializerMethodField()
    average = serializers.SerializerMethodField()
    your_rate = serializers.SerializerMethodField()

    def get_count_of_rates(self, obj: object) -> object:
        """
            Get the number of rates that every post have
        """
        return obj.rate_set.all().count()

    def get_your_rate(self, obj: object) -> object:
        """
            Get your rate
        """
        user = self.context.get('request').user
        qry_set = obj.rate_set
        if qry_set.filter(owner=user).exists():
            return qry_set.get(owner=user).score
        else:
            return None

    def get_average(self, obj: object) -> object:
        """
            Get avg of rates of post
        """
        return obj.rate_set.all().aggregate(Avg('score'))['score__avg']

    class Meta:
        model = Post
        fields = "__all__"


class RateSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Rate
        fields = ("post", "score", "owner")

    def create(self, validated_data):
        post = validated_data.get("post")
        owner = validated_data.get("owner")
        score = validated_data.get("score")

        obj, created = Rate.objects.get_or_create(
            post=post,
            owner=owner,
            defaults={"score": score}
        )
        if created:
            return obj
        else:
            obj.score = score
            obj.save()
            return obj
