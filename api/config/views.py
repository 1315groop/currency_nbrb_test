from config.models import Config
from config.models import Rate
from config.serializers import ConfigSerializer
from config.serializers import RateSerializer
from config.serializers import UserRegistrationSerializer
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class ConfigViewSet(viewsets.ModelViewSet):
    queryset = Config.objects.all()
    serializer_class = ConfigSerializer


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer


class UserRegistrationView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        request=UserRegistrationSerializer,
        responses={201: UserRegistrationSerializer, 400: "Error"},
        description="Endpoint for user registration",
    )
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
