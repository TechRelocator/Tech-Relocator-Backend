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
        search_query_title = self.request.query_params.get('title', None)

        if search_query_title:
            queryset = queryset.filter(title__icontains=search_query_title)

        # search by location
        search_query_location = self.request.query_params.get('location', None)

        if search_query_location:
            queryset = queryset.filter(location__icontains=search_query_location)

        # Search by salary in range
        search_query_salary = self.request.query_params.get('salary', None)
        if search_query_salary:
            queryset = queryset.filter(
                Q(salary_low__lte=search_query_salary) & Q(salary_high__gte=search_query_salary)
            )

        return queryset[:100]

class JobDataDetail(RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
