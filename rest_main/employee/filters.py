#custome filtering
from django_filters import rest_framework as filters
from .models import Employee
class EmployeeFilter(filters.FilterSet):
    po = filters.CharFilter(field_name='position', lookup_expr='icontains',label='POS')
    salary = filters.RangeFilter(field_name='salary', lookup_expr='gte')
    id_min=filters.CharFilter(method='filter_id_min',label='Minimum Employee ID')
    id_max=filters.CharFilter(method='filter_id_max',label='Maximum Employee ID')
    def filter_id_min(self, queryset, name, value):
        return queryset.filter(emp_id__gte=value)
    def filter_id_max(self, queryset, name, value):
        return queryset.filter(emp_id__lte=value)
    class Meta:
        model = Employee
        fields = [ 'po', 'salary','id_min','id_max']