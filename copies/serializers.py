from rest_framework import serializers
from .models import Copy, Loan


class CopySerializer(serializers.ModelSerializer):
    class Meta:
        model = Copy
        fields = ["id", "is_avaliable", "book", "loans", "last_loan"]
        read_only_fields = ["id", "book", "is_avaliable", "loans", "last_loan"]
        extra_kwargs = {
            "last_loan": {"allow_null": True},
        }


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = [
            "id",
            "is_active",
            "loaned_at",
            "deliver_in",
            "delivery_at",
            "copy",
            "account",
        ]
        read_only_fields = [
            "id",
            "copy",
            "loaned_at",
            "deliver_in",
            "delivery_at",
            "account",
            "is_active",
        ]
        extra_kwags = {"is_active": {"default": True}}
