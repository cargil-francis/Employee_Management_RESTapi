
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, CreateAPIView,UpdateAPIView,DestroyAPIView,RetrieveUpdateDestroyAPIView
from .serializer import EmpModelSerializer,EmpLeaveModelSerializer,EmpnameSerializer
from ems.models import Employee ,Emp_Leave_appilcation
from django.views.generic import DetailView
import django_filters.rest_framework
from rest_framework import filters
from rest_framework.permissions import IsAdminUser



class EmpListView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmpModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['Ename', 'Position']
    permission_classes = [IsAdminUser]
   

    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.query_params.get('ordering')
        if ordering:
            queryset = queryset.order_by(ordering)
        return queryset
    

class EmpCreateView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmpModelSerializer
    permission_classes = [IsAdminUser]


class EmpDeleteview(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmpModelSerializer
    lookup_field = 'id'
    permission_classes = [IsAdminUser]

class EmpDetailview(DetailView):
    queryset = Employee.objects.all()
    model = Employee
    serializer_class = EmpModelSerializer
    template_name = 'employee_detail.html'
    lookup_field = 'pk'
    permission_classes = [IsAdminUser]

   
class EmpUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmpModelSerializer
    lookup_field = 'id'
    permission_classes = [IsAdminUser]


class EmpLeave_View(ListAPIView):
    queryset = Emp_Leave_appilcation.objects.all()
    serializer_class = EmpLeaveModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id','Empid__Ename']
    permission_classes = [IsAdminUser]


    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.query_params.get('ordering')
        if ordering:
            queryset = queryset.order_by(ordering)
        return queryset


class EmpLeave_create(CreateAPIView):
    queryset = Emp_Leave_appilcation.objects.all()
    serializer_class = EmpLeaveModelSerializer,EmpnameSerializer
    lookup_field = 'id'



class EmpLeave_request(RetrieveUpdateDestroyAPIView):
    queryset = Emp_Leave_appilcation.objects.all()
    serializer_class = EmpLeaveModelSerializer
    lookup_field = 'id'
    permission_classes = [IsAdminUser]
    



   


    