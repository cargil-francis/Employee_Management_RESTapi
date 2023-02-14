

from rest_framework.generics import ListAPIView, CreateAPIView,UpdateAPIView,DestroyAPIView,RetrieveUpdateDestroyAPIView,RetrieveAPIView
from .serializer import EmpModelSerializer,EmpLeaveModelSerializer,EmpnameSerializer,UpdateModelSerializer
from ems.models import Employee ,Emp_Leave_appilcation
from django.views.generic import DetailView
from rest_framework import filters
from rest_framework.permissions import IsAdminUser
from rest_framework import permissions,views
from django.views import View
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView






class ObtainTokenPairWithCookieView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = response.data['access']
        print(token)
        response.set_cookie('jwt', token, max_age=3600, httponly=True)
        return response

class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        response = JsonResponse({'message': 'Successfully logged out'}, status=200)
        response.delete_cookie('jwt')
        return response
        


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

    def delete(self, request, *args, **kwargs):
        response = JsonResponse({'message': 'User Deleted Sucessfully'}, status=200)
        return response

class EmpDetailview(RetrieveAPIView):
    queryset = Employee.objects.all()
    model = Employee
    serializer_class = EmpModelSerializer
    template_name = 'employee_detail.html'
    lookup_field = 'Ename'
    permission_classes = [IsAdminUser]

   
class EmpUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = UpdateModelSerializer
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
    serializer_class = EmpLeaveModelSerializer
    
    



class EmpLeave_request(RetrieveUpdateDestroyAPIView):
    queryset = Emp_Leave_appilcation.objects.all()
    serializer_class = EmpLeaveModelSerializer
    lookup_field = 'id'
    permission_classes = [IsAdminUser]

    



   


    