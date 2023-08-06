from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import APIException, AuthenticationFailed

from .serializers import ProfileSerializer
from account.models import Profile


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


class ProfileRetrieveAPIView(APIView):
    serializer_class = ProfileSerializer
    lookup_field = 'user__username'
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def get_queryset(self):
        user = self.request.user
        requested_user = self.kwargs['user__username']

        if user.username == requested_user:
            return Profile.objects.filter(user__username=user)
        elif not Profile.objects.filter(user__username=requested_user).exists():
            raise APIException('The profile does not exist')
        else:
            raise AuthenticationFailed('You are not authorized to view this profile')

    def get(self, request, user__username):
        profile = self.get_queryset().first()
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)


class ProfileEditAPIView(ProfileRetrieveAPIView):

    def put(self, request, user__username):
        profile = self.get_queryset().first()
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Profile updated successfully'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

