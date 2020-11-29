from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import Context
from django.views.generic import TemplateView

from emp.forms import EmpForm
from emp.models import Employees


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context


def list_(request):
    emp_list = Employees.objects.all().order_by('-employee_id')[:5]
    context = {'emp_list': emp_list}
    # return render(request, 'emp/list.html', context)
    return JsonResponse(list(emp_list.values()), safe=False)


def details(request, employee_id):
    emp = get_object_or_404(Employees, pk=employee_id)
    # context = {'emp': emp}
    context = {'emp': EmpForm(instance=emp)}
    return render(request, 'emp/details.html', context)


def delete(request, employee_id):
    get_object_or_404(Employees, pk=employee_id).delete()
    return redirect('/emp/list')


def update(request):
    if request.method == 'GET':
        emp_form = EmpForm()
    else:
        try:
            emp = Employees.objects.get(employee_id=request.POST['employee_id'])
        except ObjectDoesNotExist:
            emp_form = EmpForm(request.POST)
        else:
            emp_form = EmpForm(request.POST, instance=emp)

        if emp_form.is_valid():
            print('form is valid')
            emp_form.save()
            return redirect('/emp/list')
        else:
            print('form is not valid')
    return redirect('/emp/list')
