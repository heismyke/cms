from rest_framework.views import APIView
from cms.models import cms
from cms.api.serializers import CmsSerializer
from rest_framework.response import Response
from rest_framework import status

class contacts(APIView):
    def get(self, request):
        queryset = cms.objects.all()
        serializer = CmsSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CmsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class contactDetails(APIView):
    def get(self, request, pk):
        try:
            queryset = cms.objects.get(pk=pk)
            serializer = CmsSerializer(queryset)
            return Response(serializer.data)
        except cms.DoesNotExist:
            return Response({"error": "contact not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        queryset = cms.objects.get(pk=pk)
        serializer = CmsSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            queryset = cms.objects.get(pk=pk)
            queryset.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except cms.DoesNotExist:
            return Response({"error": "contact not found"}, status=status.HTTP_404_NOT_FOUND)
