from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUserModel
from .serializers import AccountRegisterSerializer, AccountSerializer


@extend_schema(
    methods=["post"],
    request=AccountRegisterSerializer,
    responses={201: AccountSerializer, 400: "Bad Request"},
)
@api_view(["POST"])
def register_user(request: Request):
    serializer = AccountRegisterSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(
            {"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )
    try:
        user = CustomUserModel.objects.create_user(
            email=serializer.validated_data.get("email"),
            password=serializer.validated_data.get("password"),
        )
        if not user.is_active:
            return Response(
                {"error": "The user is not active"}, status=status.HTTP_401_UNAUTHORIZED
            )

        response_serializer = AccountSerializer(user)
        return Response(
            {
                "message": "User registered sucessfully!",
                "user": response_serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )

    except Exception as e:
        return Response(
            {"error": f"Some error occured {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@extend_schema(
    methods=["post"],
    request=AccountRegisterSerializer,
    responses={201: AccountSerializer, 400: "Bad Request"},
)

@api_view(["POST"])
def login(request: Request):
    serializer = AccountRegisterSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(
            {"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )
    try:
        user = authenticate(
            request,
            email=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )
        # Generate a JWT access and Refresh token for this user

        if not user:
            return Response(
                {"error": "Invalid email or password."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        refresh = RefreshToken.for_user(user)

        response_serializer = AccountSerializer(user)
        return Response(
            {
                "message": "Login sucessfully!",
                "user": response_serializer.data,
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            },
            status=status.HTTP_200_OK,
        )
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
