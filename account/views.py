from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(["POST",])
def logout(request):
  if request.method == "POST":
    request.auth_token.delete()
    return Response({"message": "Logout Successful"}, status=status.HTTP_200_OK)