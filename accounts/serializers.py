from rest_framework import serializers
from .models import Account
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from tasks.models import Task


User = get_user_model()


  
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'email', 'username', 'first_name', 'last_name']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['email', 'username', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Account.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        user = Account.objects.filter(email=email).first()

        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return {
                'email': user.email,
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }
        raise serializers.ValidationError("Invalid credentials")



class UserProfileSerializer(serializers.ModelSerializer):
    tasks_created = serializers.SerializerMethodField()
    tasks_assigned = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'tasks_created', 'tasks_assigned']

    def get_tasks_created(self, obj):
        return obj.tasks_created.values('id', 'title', 'status', 'priority', 'due_date')

    def get_tasks_assigned(self, obj):
        return obj.tasks_assigned.values('id', 'title', 'status', 'priority', 'due_date')