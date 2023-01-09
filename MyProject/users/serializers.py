from rest_framework.serializers import HyperlinkedModelSerializer
from .models import User

# lesson_1


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
