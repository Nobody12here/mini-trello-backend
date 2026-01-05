from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from .models import CustomUserModel
from .serializers import AccountRegisterSerializer, AccountSerializer


@swagger_auto_schema(
    method="post",
    request_body=AccountRegisterSerializer,
    responses={201: AccountSerializer, 400: "Bad Request"},
)
@api_view(["POST"])
def register_user(request: Request):
    serializer = AccountRegisterSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(
            {"error": serializer.error_messages}, status=status.HTTP_400_BAD_REQUEST
        )
    try:
        user = CustomUserModel.objects.create_user(
            email=serializer.validated_data.get("email"),
            password=serializer.validated_data.get("password"),
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


@api_view()
def test_view(request):
    return Response("Hello world")
