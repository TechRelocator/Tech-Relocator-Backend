from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import User_Profile
from .serializer import UserProfileSerializer
from .permissions import IsOwner

class UserProfileList(ListCreateAPIView):
    permission_classes = (IsOwner,)
    queryset = User_Profile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwner,)
    queryset = User_Profile.objects.all()
    serializer_class = UserProfileSerializer
