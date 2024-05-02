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
    path('department/create/', views.CreateDepartmentViewSet.as_view({'post': 'create'})),
    path('department/profile/<int:pk>/', views.DepartmentView.as_view({'get': 'retrieve'})),
    path('department/<int:pk>/', views.CreateDepartmentViewSet.as_view({'patch': 'partial_update'})),
    path('department/delete/<int:pk>/', views.DepartmentView.as_view({'delete': 'destroy'})),
    path('departments/<int:unit_id>/', views.DepartmentListView.as_view(), name='department-list'),

    # Employee
    path('employee/', views.EmployeeView.as_view({'get': 'list'})),
    path('employee/create/', views.CreateEmployeeViewSet.as_view({'post': 'create'})),
    path('employee/profile/<int:pk>/', views.EmployeeView.as_view({'get': 'retrieve'})),
    path('employee/<int:pk>/', views.CreateEmployeeViewSet.as_view({'patch': 'partial_update'})),
    path('employee/delete/<int:pk>/', views.EmployeeView.as_view({'delete': 'destroy'})),

    #Dashboard
    path('record-count/', views.RecordCountView.as_view(), name='record-count'),
]