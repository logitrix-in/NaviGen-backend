from rest_framework.serializers import ModelSerializer
from authentication.models import User


class UserSerialisers(ModelSerializer):
    class Meta:
        model = User
        # fields="__all__"
        exclude = ["password",]
