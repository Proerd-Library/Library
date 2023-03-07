from rest_framework import serializers
from .models import Account
from rest_framework.validators import UniqueValidator


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "id",
            "email",
            "password",
            "username",
            "created_at",
            "updated_at",
            "following",
            "copies",
            "is_colaborator",
            "is_superuser"
        ]
        read_only_fields = ["id", "created_at", "updated_at", "following", "copies", "is_superuser"]
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {
                "validators": [
                    UniqueValidator(
                        queryset=Account.objects.all(),
                        message="A user with that email already exists.",
                    )
                ]
            },
            "username": {
                "validators": [
                    UniqueValidator(
                        queryset=Account.objects.all(),
                        message="A user with that username already exists.",
                    )
                ]
            },
            "is_colaborator": {"allow_null": True, "default": False}
        }
