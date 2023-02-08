from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import EmpListView, EmpCreateView,EmpUpdateView,EmpDeleteview

urlpatterns = [
    path('employee/', EmpListView.as_view(), name='emp-list'),
    path('employee/create/', EmpCreateView.as_view(), name='emp-create'),
    path('employee/update/',EmpUpdateView.as_view(),name='emp-update'),
    path('employee/delete/',EmpDeleteview.as_view(),name='emp-delete')

]

urlpatterns = format_suffix_patterns(urlpatterns)