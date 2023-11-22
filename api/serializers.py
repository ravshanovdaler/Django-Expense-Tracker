from rest_framework import serializers
from users.models import UserModel
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(min_length=8, style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = UserModel
        fields = ('username', 'email', 'first_name', 'last_name', 'age', 'Job', 'phone_number', 'password', 'password2')

    def validate(self, attrs):
        user_exists = UserModel.objects.filter(username=attrs['username']).exists()
        if user_exists:
            raise ValidationError('User already exists')
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise ValidationError('Passwords do not match')

        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop('password')
        password2 = validated_data.pop('password2')
        if password != password2:
            raise ValidationError('Passwords do not match')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user
