from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.employee_form,name='insert'),
    path('<int:id>/',views.employee_form,name='update'),
    path('list/',views.employee_list,name='view'),
    path('Delete/<int:id>/',views.employee_delete,name="delete")
]
