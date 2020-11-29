from django.shortcuts import render
from django.views.generic import TemplateView
from emp.models import Employees


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context


def list_(request):
    emp_list = Employees.objects.all().order_by('-employee_id')[:5]
    context = {'emp_list': emp_list}
    return render(request, 'list.html', context)
