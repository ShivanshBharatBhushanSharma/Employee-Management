from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Employee


class AddEmployeeAPIView(CreateAPIView):
    serializer_class = EmployeeSerializer

    def post(self,request):
        serializer = self.get_serializer(data=request.data) 

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class EmployeeListView(ListAPIView) :
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    def get(self, request, *args, **kwargs):
        Employee_serializers = super().list(request, *args, **kwargs)

        return Response(Employee_serializers.data, status.HTTP_200_OK)

class UpdateEmployeeAPIView(UpdateAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        return Employee.objects.filter(id=self.kwargs["pk"])

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
              
        instance.Name = request.data["Name"]
        instance.Department = request.data["Department"]
        instance.Designation = request.data["Designation"]
        instance.Salary = request.data["Salary"]
        instance.Hiring_date = request.data["Hiring_date"]
    
        Employee_serializer = self.get_serializer(instance, data=request.data)
        if Employee_serializer.is_valid(raise_exception=True):
            self.partial_update(Employee_serializer)

            return Response(Employee_serializer.data, status.HTTP_200_OK)
        return Response(Employee_serializer.errors, status.HTTP_400_BAD_REQUEST)

class DeleteEmployeeRecordAPIView(DestroyAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        employee_id = self.kwargs["pk"]
        return Employee.objects.filter(id=employee_id)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()

            return Response({"data": None, "message": "Employee deleted successfully.",
                             "status": status.HTTP_200_OK, "error": None})
        except Employee.DoesNotExist:
            return Response({"data": None, "message": "Employee not found.",
                             "status": status.HTTP_404_NOT_FOUND, "error": None})    
