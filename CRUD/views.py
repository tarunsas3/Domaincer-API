from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer
from .models import User
from rest_framework.permissions import IsAuthenticated, AllowAny

class UserView(APIView):

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        elif self.request.method == 'POST':
            return [IsAuthenticated()]
        elif self.request.method in ['PUT', 'DELETE']:
            return [IsAuthenticated()]
        return super().get_permissions()

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"})
        return Response({"error": "Failed to create User"}, status=400)

    def get(self, request, pk=None):
        if pk:
            user = get_object_or_404(User, userId=pk)
            serializer = UserSerializer(user)
        else:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def put(self, request, pk=None):
        user = get_object_or_404(User, userId=pk)
        serializer = UserSerializer(instance=user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User updated successfully"})
        return Response({"error": "Failed to update User"}, status=400)

    def delete(self, request, pk=None):
        user = get_object_or_404(User, userId=pk)
        user.delete()
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({"message": "User deleted successfully"}, status=200)
