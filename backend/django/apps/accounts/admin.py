from django.contrib import admin
# from polymorphic.admin import PolymorphicParentModelAdmin, \
#        PolymorphicChildModelAdmin, PolymorphicChildModelFilter
# from .models import AbstractAccount
from .models import BaseAccount

admin.site.register(BaseAccount)

#  @admin.register(AbstractAccount)
#  class ParentAccountAdmin(PolymorphicParentModelAdmin):
#      """ Parent model admin """
#      base_model = AbstractAccount
#      child_models = (BaseAccount,)
#      list_filter = (PolymorphicChildModelFilter,)
#
#
#  @admin.register(BaseAccount)
#  class OrdinaryAccountAdmin(PolymorphicChildModelAdmin):
#      """ BaseAccount admin """
#      base_model = BaseAccount
