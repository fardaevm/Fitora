from rest_framework import generics, permissions
from .models import Weight
from .serializers import WeightSerializer


class WeightListCreate(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    # queryset = Weight.objects.all()
    serializer_class = WeightSerializer

    def get_queryset(self):
        # Check if 'user_id' is passed as a query parameter
        # user = self.request.query_params.get('user')
        # if user:
        return Weight.objects.filter(user=self.request.user)
        # return Weight.objects.none()

    def perform_create(self, serializer):
        # When creating a new weight entry, assign the logged-in user as the owner
        serializer.save(user=self.request.user)

class WeightDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = WeightSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Weight.objects.all()
        # Only return the weight entries of the logged-in user
        return Weight.objects.filter(user=self.request.user)