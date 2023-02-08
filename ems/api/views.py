

from rest_framework.generics import ListAPIView, CreateAPIView,UpdateAPIView,DestroyAPIView


from .serializer import EmpModelSerializer
from ems.models import Employee


class EmpListView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmpModelSerializer

class EmpCreateView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmpModelSerializer

class EmpUpdateView(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmpModelSerializer
    
class EmpDeleteview(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmpModelSerializer
