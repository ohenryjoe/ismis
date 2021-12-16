from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from acl.models import User
from hrms.forms import EmployeeForm, DesignationForm, DesignationsForm
from hrms.models import Employees, Directorates, Divisions, Departments, Sections, Designations

from django.http import JsonResponse


@login_required
def designation_list(request):
    designation = Designations.objects.all()
    return JsonResponse({'data': [{'id': p.id, 'title': p.name} for p in designation]})


@login_required
def directorate_list(request):
    directorate = Directorates.objects.all()
    return JsonResponse({'data': [{'id': q.id, 'title': q.name} for q in directorate]})


@login_required
def department_list(request, directorate_id):
    department = Departments.objects.filter(directorate_id=directorate_id)
    return JsonResponse({'data': [{'id': r.id, 'title': r.name} for r in department]})


@login_required
def division_list(request, department_id):
    division = Divisions.objects.filter(department_id=department_id)
    return JsonResponse({'data': [{'id': s.id, 'title': s.name} for s in division]})


@login_required
def section_list(request, division_id):
    section = Sections.objects.filter(division_id=division_id)
    return JsonResponse({'data': [{'id': t.id, 'title': t.name} for t in section]})


@login_required()
def New_Designation(request):
    user = User.pk
    if request.method == 'POST':
        form = DesignationsForm()
        if form.is_valid():
            obj = form.save()
            obj.update(created_by=user)
            messages.success(request, "Equated Adult Code added successfully!")
            return render(
                request,
                'hrms/EmployeeDashboard.html',
            )
        else:
            messages.success(request, "Error!")
            pass
    else:
        form = DesignationForm()
        return render(
            request,
            'hrms/designationform.html',
            {'form': form, 'user': user}
        )
        # return HttpResponse('<script type="text/javascript">window.close(); window.parent.location.href = '
        #                 '"/";</script>')


class EmployeesListView(ListView):
    model = Employees
    context_object_name = 'employee'
    template_name = 'employee_list.html'


class EmployeesCreateView(CreateView):
    model = Employees
    form_class = EmployeeForm
    template_name = 'hrms/employeeform.html'
    success_url = reverse_lazy('person_changelist')


class EmployeesUpdateView(UpdateView):
    model = Employees
    form_class = EmployeeForm
    template_name = 'hrms/employeeform.html'
    success_url = reverse_lazy('person_changelist')


class DesignationsListView(ListView):
    model = Designations
    context_object_name = 'designation'
    template_name = 'employee_list.html'


class DesignationsCreateView(CreateView):
    model = Designations
    form_class = DesignationForm
    template_name = 'hrms/designationform.html'
    success_url = reverse_lazy('person_changelist')


class DesignationsUpdateView(UpdateView):
    model = Designations
    form_class = DesignationForm
    template_name = 'hrms/designationform.html'
    success_url = reverse_lazy('person_changelist')


def load_departments(request):
    directorate_id = request.GET.get('id_directorate')
    departments = Departments.objects.filter(directorate_id=directorate_id)
    context = {'departments': departments}
    return render(request, 'hrms/department_dropdownlist_options.html', context)


def load_divisions(request):
    department_id = request.GET.get('department')
    divisions = Divisions.objects.filter(department_id_id=department_id).order_by('name')
    context = {'divisions': divisions}
    return render(request, 'hrms/division_add.html', context)


def load_sections(request):
    divison_id = request.GET.get('division')
    sections = Sections.objects.filter(divison_id=divison_id).order_by('name')
    return render(request, 'hrms/sectionform.html', {'sections': sections})


# Create your views here.
@login_required()
def dashboard(request):
    curruser = get_object_or_404(User, pk=request.user.pk)
    curruser = curruser.is_admin
    if curruser:
        return render(request, 'hrms/DirectorateDashboard.html', {'curruser': curruser})
    else:
        return render(request, 'hrms/EmployeeDashboard.html', {'curruser': curruser})


@login_required()
def employees(request):
    return
