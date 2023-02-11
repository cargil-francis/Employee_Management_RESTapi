from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import EmpListView, EmpCreateView,EmpUpdateView,EmpDeleteview,EmpDetailview,RetrieveUpdateDestroyAPIView,EmpLeave_View
from .views import EmpLeave_View,EmpLeave_create,EmpLeave_request


urlpatterns = [
    path('employee/', EmpListView.as_view(), name='emp-list'),
    path('employee/create/', EmpCreateView.as_view(), name='emp-create'),
    path('employee/delete/<int:id>',EmpDeleteview.as_view(), name='emp-delete'),
    path('employee/detail/<int:pk>/',EmpDetailview.as_view(), name='emp-detail'),
    path('employee/update/<int:id>',EmpUpdateView.as_view(), name='emp-update'),

    path('employee/leave/',EmpLeave_View.as_view(), name='emp-leave'),
    path('employee/leavecreate/',EmpLeave_create.as_view(),name='emp-leave-create'),
    path('employee/leaverequest/<int:id>',EmpLeave_request.as_view(), name='emp-leave-request'),
   

]

urlpatterns = format_suffix_patterns(urlpatterns)