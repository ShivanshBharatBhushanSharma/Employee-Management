from django.conf.urls import url
from .views import AddEmployeeAPIView, UpdateEmployeeAPIView, EmployeeListView, DeleteEmployeeRecordAPIView

urlpatterns = [
    url("addEmployee",AddEmployeeAPIView.as_view(), name="add-Employee"),
    url("getEmployeeList",EmployeeListView.as_view(), name="get-Employee"),
    url("updateEmployee/(?P<pk>.+)",UpdateEmployeeAPIView.as_view(), name="update-Employee"),
    url("deleteEmployee/(?P<pk>.+)",DeleteEmployeeRecordAPIView.as_view(), name="delete-Employee")

]    
