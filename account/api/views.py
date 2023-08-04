from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework import status


class SignupAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        username = data['username']
        password = data['password']
        password2 = data['password2']
        email = data['email']

        if password == password2:
            if User.objects.filter(username=username).exists():
                return Response({'error': 'Username already exists'})
            else:
                user = User.objects.create(username=username, email=email)
                user.set_password(password)
                user.save()
                return Response({'detail': 'User created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        username = data['username']
        password = data['password']

        user = authenticate(username=username, password=password)

        if user is None:
            return Response({'error': 'Incorrect Username/Password'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            login(request, user)
            return Response({'detail': 'Successfully logged in'}, status=status.HTTP_200_OK)


class LogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)
    def get(self, request):
        print(request.user)
        logout(request)
        return Response({'detail': 'Successfully logged out'}, status=status.HTTP_200_OK)