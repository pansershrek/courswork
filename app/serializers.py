from rest_framework import serializers
from .models import Texts


class TextsListSerializer(serializers.ListSerializer):

    def to_internal_value(self):
        internal_value = []
        for data in self.data:
            serialized = TextsSerializers(data)
            internal_value.append(serialized.to_internal_value())
        return internal_value


class TextsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Texts
        fields = ('title', )
        list_serializer_class = TextsListSerializer

    def to_internal_value(self):
        return self.data['title']
