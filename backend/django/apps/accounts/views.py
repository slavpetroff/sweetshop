from core.base_viewset import BaseViewSet
from .models import AbstractAccount

from .serializers import WholeAccountSerializer


class AccountViewSet(BaseViewSet):
    queryset = AbstractAccount.objects.all()
    serializer_class = WholeAccountSerializer
