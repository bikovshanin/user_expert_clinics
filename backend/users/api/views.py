from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from users.models import User
from .permissions import IsAuthenticatedOwnerOrAdmin
from .serializers import UserSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = (
        'last_name',
        'first_name',
        'middle_name',
        'phone_number',
        'email',
    )


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOwnerOrAdmin,)
