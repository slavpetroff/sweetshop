from rest_framework import serializers
from .models import AbstractAccount


class WholeAccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = AbstractAccount
        fields = ('id', 'first_name', 'last_name', 'email', 'password',
                  'telephone', 'address', 'last_activity_at',
                  'last_activity_at',)

    def create(self, validated_data):
        return AbstractAccount.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return AbstractAccount.objects.update_user(
            instance=instance, validated_data=validated_data)
