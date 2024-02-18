from cms.models import cms
from rest_framework import serializers


class CmsSerializer(serializers.ModelSerializer):

    class Meta:
        model = cms
        fields = "__all__"