from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, \
        PolymorphicChildModelAdmin, PolymorphicChildModelFilter
from .models import AbstractAccount


class BaseAccountAdmin(PolymorphicChildModelAdmin):
    """ Base admin class for all child models """
    base_model = AbstractAccount


@admin.register(AbstractAccount)
class ParentAccountAdmin(PolymorphicParentModelAdmin):
    """ The parent model admin """
    base_model = AbstractAccount
    child_models = (AbstractAccount,)
    list_filter = (PolymorphicChildModelFilter,)
