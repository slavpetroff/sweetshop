from rest_framework import serializers
from .models import BaseAccount


class WholeAccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = BaseAccount
        fields = ('id', 'first_name', 'last_name', 'email', 'password',
                  'phone_number', 'address', 'last_activity_at',
                  'last_activity_at',)

    def create(self, validated_data):
        return BaseAccount.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        return BaseAccount.objects.update_user(
            instance=instance, validated_data=validated_data)
