from django.urls import path
from .views import  EmployeeClassBasedView,EmployeeClassBasedDetailsView
urlpatterns = [
    path('emp/<int:id>', EmployeeClassBasedDetailsView.as_view() ),
    path('emp/all', EmployeeClassBasedView.as_view() ),
]