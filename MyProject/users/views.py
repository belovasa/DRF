from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserModelSerializer

# lesson_1


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
