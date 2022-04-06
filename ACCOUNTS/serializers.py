from rest_framework import serializers

from ACCOUNTS.models import CustomUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

User = get_user_model()

from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class SignupSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id','name', 'password', 'password2', 'email','type','groups')
        extra_kwargs = {
            'name': {'required': True},
            'type': {'required': True},
            'groups': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        groups = validated_data.pop('groups', ())


        user = User.objects.create(
            name=validated_data['name'],
            email=validated_data['email'],
            password=validated_data['password'],
            type=validated_data['type'],
            
        )
        if user.type=='admin':
            user.type = 'admin'
            user.is_staff = True
            user.is_superuser = True
         # add groups to the user ↓
        user.groups.add(*groups)

        user.set_password(validated_data['password'])
        user.save()

        return user
    
    def validated_name(self,value):
        if value!=None:
            raise serializers.ValidationError("name must be enter")
        return value

    def validated_groups(self,value):
        if value!=None:
            raise serializers.ValidationError("groups must be enter")
        return value
