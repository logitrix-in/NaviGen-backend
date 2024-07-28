from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from django.contrib.auth.hashers import make_password
from authentication.models import User
from authentication.serializers import UserSerialisers


class AuthView(APIView):
    # Current User
    def get(self, request):
        try:
            db = User.objects.get(
                id=request.COOKIES.get('uid')
            )
            data = UserSerialisers(db).data
            return Response(data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"message": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)
    # register
    def put(self, request):
        user_name = request.data.get('username', None)
        password = request.data.get('password', None)
        phone_number = request.data.get('phone_number', None)
        email = request.data.get('email', None)
        first_name = request.data.get('first_name', None)
        last_name = request.data.get('last_name', None)
        profile_picture = request.data.get('profile_picture', None)

        if user_name and password and phone_number and email and first_name and last_name:
            print(user_name, password, phone_number,
                  email, first_name, last_name)
            user, created = User.objects.get_or_create(username=user_name)
            if created:
                user.username = user_name
                user.password = make_password(password)
                user.phone_number = phone_number
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                user.profile_picture = profile_picture
                user.is_staff = True
                user.is_active = True
                user.save()
                return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "User already exists"}, status=status.HTTP_409_CONFLICT)
        else:
            return Response({"message": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

    # login
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        print(username, password)
        auth = authenticate(username=username, password=password)
        print(auth)
        if auth:
            response = Response(
                {"message": "Login successful"}, status=status.HTTP_200_OK)
            response.set_cookie('uid', auth.pk,
                                secure=False, httponly=True)
            return response
        else:
            return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

    # logout
    def delete(self, request):
        response = Response({"message": "Logout successful"},
                            status=status.HTTP_200_OK)
        response.delete_cookie('uid')
        return response
