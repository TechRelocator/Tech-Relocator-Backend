from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Job
from .serializer import JobSerializer


class JobDataList(ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)
        return queryset[:100]

class JobDataDetail(RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer