from rest_framework.serializers import\
    ModelSerializer
from graph.models import *


class SimpleNodeSerializer(ModelSerializer):
    class Meta:
        model = Node
        fields = (
            'id',
            'name',
        )
        read_only_fields = fields
