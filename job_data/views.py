from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Job
from .serializer import JobSerializer
from django.db.models import Q


class JobDataList(ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        # search by title
        search_query = self.request.query_params.get('title', None)

        if search_query:
            queryset = queryset.filter(title__icontains=search_query)

        # search by location
        search_query = self.request.query_params.get('location', None)

        if search_query:
            queryset = queryset.filter(location__icontains=search_query)

        # Search by salary in range
        salary_search = self.request.query_params.get('salary', None)
        if salary_search:
            queryset = queryset.filter(
                Q(salary_low__lte=salary_search) & Q(salary_high__gte=salary_search)
            )

        return queryset[:100]

class JobDataDetail(RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
