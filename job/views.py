from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from .models import Job
from .serializers import JobSerializer

class JobListView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            jobs = Job.objects.all()
            serializer = JobSerializer(jobs, many=True)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
        except Job.DoesNotExist:
            return JsonResponse({"error": "Jobs not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class JobDetailView(APIView):
    def get_object(self, pk):
        try:
            return Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):
        job = self.get_object(pk)
        if job is not None:
            serializer = JobSerializer(job)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        else:
            return JsonResponse({"error": "Job not found"}, status=status.HTTP_404_NOT_FOUND)