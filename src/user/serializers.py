from rest_framework import serializers
from .models import User
import bcrypt


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "phone_no",
            "password",
            "pic_path",
        )

    def create(self, validated_data):
        salt = self.saltSecret()
        user = User.objects.create(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            phone_no=validated_data["phone_no"],
            password=bcrypt.hashpw(
                validated_data["password"].encode("utf8"), salt),
        )
        return user

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_no = validated_data.get('phone_no', instance.phone_no)
        instance.save()
        return instance

    def saltSecret(self):
        return bcrypt.gensalt()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "phone_no",
            "pic_path",
        )
