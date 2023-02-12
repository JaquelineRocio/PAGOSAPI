from django.contrib.auth import authenticate
from rest_framework import status, generics,viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from .serializers import RegisterSerializer, GetUserSerializer
from .tokens import create_jwt
from .models import User


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request: Request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                "message": "Usuario creado",
                "body": serializer.data,
            }

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):

    def post(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)
        if user is not None:
            tokens = create_jwt(user)
            data={
                "id":user.id,
                "email":email,
                "username":user.username,
                "isAdmin": user.is_staff
            }
            response = {"message": "Logeado correctamente", "body":data ,"tokens": tokens}
            return Response(data=response, status=status.HTTP_200_OK)

        else:
            return Response(data={"message": "Email inválido o password incorrecto"},status=status.HTTP_400_BAD_REQUEST)

    def get(self, request: Request):
        content = {"user": str(request.user), "auth": str(request.auth)}

        return Response(data=content, status=status.HTTP_200_OK)

class GetUsers(viewsets.ReadOnlyModelViewSet):
    serializer_class = GetUserSerializer
    queryset = User.objects.all()


