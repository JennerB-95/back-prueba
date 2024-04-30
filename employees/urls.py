from django.urls import path
from employees import views

app_name = 'employees'

urlpatterns = [
    # Unit
    path('unit/', views.UnitView.as_view({'get': 'list'})),
    path('unit/create/', views.UnitView.as_view({'post': 'create'})),
    path('unit/profile/<int:pk>/', views.UnitView.as_view({'get': 'retrieve'})),
    path('unit/<int:pk>/', views.UnitView.as_view({'patch': 'partial_update'})),
    path('unit/delete/<int:pk>/', views.UnitView.as_view({'delete': 'destroy'})),

    # Department
    path('department/', views.DepartmentView.as_view({'get': 'list'})),
    path('department/create/', views.DepartmentView.as_view({'post': 'create'})),
    path('department/profile/<int:pk>/', views.DepartmentView.as_view({'get': 'retrieve'})),
    path('department/<int:pk>/', views.DepartmentView.as_view({'patch': 'partial_update'})),
    path('department/delete/<int:pk>/', views.DepartmentView.as_view({'delete': 'destroy'})),

    # Employee
    path('employee/', views.EmployeeView.as_view({'get': 'list'})),
    path('employee/create/', views.EmployeeView.as_view({'post': 'create'})),
    path('employee/profile/<int:pk>/', views.EmployeeView.as_view({'get': 'retrieve'})),
    path('employee/<int:pk>/', views.EmployeeView.as_view({'patch': 'partial_update'})),
    path('employee/delete/<int:pk>/', views.EmployeeView.as_view({'delete': 'destroy'})),
]