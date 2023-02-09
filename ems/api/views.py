
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, CreateAPIView,UpdateAPIView,DestroyAPIView,RetrieveUpdateDestroyAPIView
from .serializer import EmpModelSerializer
from ems.models import Employee
from django.views.generic import DetailView
import django_filters.rest_framework
from rest_framework import filters


class EmpListView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmpModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['Ename', 'Position']

    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.query_params.get('ordering')
        if ordering:
            queryset = queryset.order_by(ordering)
        return queryset

    

    

class EmpCreateView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmpModelSerializer


class EmpDeleteview(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmpModelSerializer
    lookup_field = 'id'

class EmpDetailview(DetailView):
    queryset = Employee.objects.all()
    model = Employee
    serializer_class = EmpModelSerializer
    template_name = 'employee_detail.html'
    lookup_field = 'pk'


   
class EmpUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmpModelSerializer
    lookup_field = 'id'

#   def partial_update(self, request, *args, **kwargs):
#         kwargs['partial'] = True
#         return self.update(request, *args, **kwargs)

