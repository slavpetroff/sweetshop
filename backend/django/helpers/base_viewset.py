from rest_framework import status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class BaseViewSet(viewsets.ModelViewSet):
    true = True
    false = False
    none = None

    authentication_classes = AllowAny,

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not self.none:
            serializer = self.get_serializer(page, many=self.true)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=self.true)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)

        try:
            serializer.is_valid(raise_exception=self.true)
        except ValidationError as exception:
            invalid_fields = list(exception.detail.keys())
            message = {'invalid_input_fields': invalid_fields}
            return Response(data=message, status=status.HTTP_400_BAD_REQUEST)

        try:
            instance_to_create = serializer.create(validated_data=data)
        except Exception as exception:
            message = exception.message
            return Response(data=message, status=status.HTTP_400_BAD_REQUEST)

        serialized_instance = self.get_serializer(instance_to_create).data
        return Response(
            data=serialized_instance, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance_to_update = self.get_object()

        data = request.data

        try:
            updated_object = self.get_serializer().update(
                instance=instance_to_update, validated_data=data)
        except ValidationError as exception:
            invalid_fields = list(exception.detail.keys())
            message = {'invalid_input_fields': invalid_fields}
            return Response(data=message, status=status.HTTP_400_BAD_REQUEST)

        except ValueError:
            return Response(
                data={'message': 'Value error'},
                status=status.HTTP_400_BAD_REQUEST)

        except Exception as exception:
            return Response(
                data={'message': exception.message},
                status=status.HTTP_403_FORBIDDEN)

        serialized_instance = self.get_serializer(updated_object).data
        return Response(
            data=serialized_instance, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_200_OK)
