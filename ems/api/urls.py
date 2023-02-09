from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import EmpListView, EmpCreateView,EmpUpdateView,EmpDeleteview,EmpDetailview,RetrieveUpdateDestroyAPIView

urlpatterns = [
    path('admin/employee/', EmpListView.as_view(), name='emp-list'),
    path('admin/employee/create/', EmpCreateView.as_view(), name='emp-create'),
    path('admin/employee/delete/<int:id>',EmpDeleteview.as_view(),name='emp-delete'),
    path('admin/employee/detail/<int:pk>/',EmpDetailview.as_view(),name='emp-detail'),
    path('admin/employee/update/<int:id>',EmpUpdateView.as_view(),name='emp-update'),
   

]

urlpatterns = format_suffix_patterns(urlpatterns)