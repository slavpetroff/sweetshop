from helpers.base_viewset import BaseViewSet
from .models import BaseAccount

from .serializers import WholeAccountSerializer


class AccountViewSet(BaseViewSet):
    queryset = BaseAccount.objects.all()
    serializer_class = WholeAccountSerializer
