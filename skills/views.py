from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Skill
from .serializer import SkillSerializer


class SkillList(ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('title', None)
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)
        return queryset

class SkillDetail(RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer