from rest_framework import serializers

from weights.models import Weight


class WeightSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Weight

        fields = (
            'id',
            'user',
            'weight',
            'created_at',
            'updated_at',
        )

        read_only_fields = ('id', 'user', 'created_at', 'updated_at')

        extra_kwargs = {
            'weight': {'required': True, 'min_value': 0},  # Ensure weight is required and can't be negative
        }

