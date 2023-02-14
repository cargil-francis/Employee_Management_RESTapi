from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import EmpListView, EmpCreateView,EmpUpdateView,EmpDeleteview,EmpDetailview,RetrieveUpdateDestroyAPIView,EmpLeave_View
from .views import EmpLeave_View,EmpLeave_create,EmpLeave_request
#from knox import views as knox_views
from ems.api.views import LogoutView
from rest_framework_simplejwt.views import TokenBlacklistView



urlpatterns = [
    path('employee/', EmpListView.as_view(), name='emp-list'),
    path('employee/create/', EmpCreateView.as_view(), name='emp-create'),
    path('employee/delete/<int:id>',EmpDeleteview.as_view(), name='emp-delete'),
    path('employee/detail/<str:Ename>/',EmpDetailview.as_view(), name='emp-detail'),
    path('employee/update/<int:id>',EmpUpdateView.as_view(), name='emp-update'),
    path('employee/leave/',EmpLeave_View.as_view(), name='emp-leave'),
    path('employee/leavecreate/',EmpLeave_create.as_view(),name='emp-leave-create'),
    path('employee/leaverequest/<int:id>',EmpLeave_request.as_view(), name='emp-leave-request'),
    path('logout/',LogoutView.as_view(),name='logout'),
    


  path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),


]

urlpatterns = format_suffix_patterns(urlpatterns)