from django import forms
from hrms.models import Employees, Directorates, Divisions, Departments, Sections, Designations


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = [
            'employee_number',
            'username',
            'title',
            'first_name',
            'last_name',
            'middle_name',
            'other_names',
            'email',
            'designation',
            'gender',
            'marital_status',
            'religion',
            'dob',
            'nin',
            'passport',
            'nssf',
            'tin',
            'permit',
            'date_joined',
            'avatar',
            'exit_date',
            'nationality',
            'employee_sne_status',
            'employment_term',
            'employment_status',
            'employment_type',
        ]

        labels = {
            'employee_number': 'Employee Number',
            'username': 'Username',
            'title': 'Title',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'middle_name': 'Middle Name',
            'other_names': 'Other Names',
            'gender': 'Gender',
            'email': 'Email',
            'designation': 'Designation',
            'marital_status': 'Marital Status',
            'religion': 'Religion',
            'dob': 'Date of Birth',
            'nin': 'National ID Number',
            'passport': 'Passport Number',
            'nssf': 'NSSF Number',
            'tin': 'Tax Identification Number',
            'permit': 'Driving Permit Number',
            'date_joined': 'Date of Joining',
            'avatar': 'Profile Picture',
            'exit_date': 'Exit Date',
            'nationality': 'Nationality',
            'employee_sne_status': 'Employee SNE Status',
            'employment_term': 'Terms of Employment',
            'employment_status': 'Status of Employment',
            'employment_type': 'Type of Employment',
        }
        help_texts = {
            'employee__sne_status': 'Whether the employee is a special need and the type of special need',
            'employment_status': 'Whether the employee is in-service, retired etc',
            'employment_term': 'Employee is on Permanent, Contract,Temporary etc',
            'employment_type': 'Whether the employment is full-time, part-time,etc',
        }
        error_messages = {
            'nssf': {'max_length': "This Employee Number is too long.",
                     },
        }
        widgets = {
            'dob': forms.DateInput(attrs={'data-mask': "DD/MM/YYYY"})
        }

    def __str__(self):
        self.helper.form_show_labels = False


class DesignationForm(forms.ModelForm):
    class Meta:
        model = Designations
        fields = [
            'title',
            'short_name',
            'directorate',
            'department',
            'division',
            'section',
            'salary_scale',
            'supervisor',
            'probational',
            'probation_period',
            'job_summary',
            'job_description',
            'max_holders',
            'active',
            'headed_entity',
        ]

        labels = {
            'title': 'Title',
            'short_name': 'Short Name',
            'directorate': 'Directorate',
            'department': 'Department',
            'division': 'Division',
            'section': 'Section',
            'salary_scale': 'Salary Scale',
            'supervisor': 'Supervisor',
            'probational': 'Yes',
            'probation_period': 'Probation period',
            'job_summary': 'Job Summary',
            'job_description': 'Job Description',
            'max_holders': 'Maximum Appointees',
            'active': 'Yes',
            'headed_entity': 'Is Head of',
        }
        help_texts = {
            'short_name': 'Two or Three letters short for Designation e.g DTR',
            'supervisor': 'The job that supervises this job',
            'max_holders': 'The number officers who can be appointed to the role.'
        }
        error_messages = {
            'title': {'max_length': "This Job Title is too long.",
                      },
        }

    def __str__(self):
        self.helper.form_show_labels = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['department'].queryset = Departments.objects.none()

        if 'directorate' in self.data:
            try:
                directorate = int(self.data.get('directorate'))
                self.fields['department'].queryset = Departments.objects.filter(
                    directorate_id=directorate).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Department queryset
        elif self.instance.pk:
            self.fields['department'].queryset = self.instance.directorate.department_set.order_by('title')

        #############

        self.fields['division'].queryset = Divisions.objects.none()
        if 'department' in self.data:
            try:
                department = int(self.data.get('department'))
                self.fields['division'].queryset = Divisions.objects.filter(department=department).order_by(
                    'name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['division'].queryset = self.instance.directorate.department_set.order_by('title')

        self.fields['section'].queryset = Sections.objects.none()
        if 'division' in self.data:
            try:
                division = int(self.data.get('division'))
                self.fields['division'].queryset = Sections.objects.filter(division=division).order_by('title')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['section'].queryset = self.instance.division.section_set.order_by('title')


class DesignationsForm(forms.ModelForm):
    class Meta:
        model = Designations

        fields = [
            'title',
            'short_name',
            'directorate',
            'department',
            'division',
            'section',
            'salary_scale',
            'supervisor',
            'probational',
            'probation_period',
            'job_summary',
            'job_description',
            'max_holders',
            'active',
            'headed_entity',
        ]

        labels = {
            'title': 'Title',
            'short_name': 'Short Name',
            'directorate': 'Directorate',
            'department': 'Department',
            'division': 'Division',
            'section': 'Section',
            'salary_scale': 'Salary Scale',
            'supervisor': 'Supervisor',
            'probational': 'Yes',
            'probation_period': 'Probation period',
            'job_summary': 'Job Summary',
            'job_description': 'Job Description',
            'max_holders': 'Maximum Appointees',
            'active': 'Yes',
            'headed_entity': 'Is Head of',
        }
        help_texts = {
            'short_name': 'Two or Three letters short for Designation e.g DTR',
            'supervisor': 'The job that supervises this job',
            'max_holders': 'The number officers who can be appointed to the role.'
        }

    def __init__(self, *args, **kwargs):
        super(DesignationsForm, self).__init__(*args, **kwargs)
        try:
            self.initial['directorate'] = kwargs['instance'].directorate.id
        except:
            pass
        directorate_list = [('', '---------')] + [(i.id, i.name) for i in Directorates.objects.all()]

        # Department, Division,Section is on the child level, it will be loaded when user click the parent level
        try:
            self.initial['department'] = kwargs['instance'].department.id
            department_init_form = [(i.id, i.name) for i in Departments.objects.filter(
                directorate=kwargs['instance'].directorate
            )]
        except:
            department_init_form = [('', '---------')]

        try:
            self.initial['division'] = kwargs['instance'].division.id
            division_init_form = [(i.id, i.name) for i in Divisions.objects.filter(
                department=kwargs['instance'].department
            )]
        except:
            division_init_form = [('', '---------')]

        try:
            self.initial['section'] = kwargs['instance'].section.id
            kelurahan_init_form = [(i.id, i.name) for i in Sections.objects.filter(
                division=kwargs['instance'].division
            )]
        except:
            section_init_form = [('', '---------')]

        # Override the form, add onchange attribute to call the ajax function
        self.fields['directorate'].widget = forms.Select(
            attrs={
                'id': 'id_directorate',
                'onchange': 'getDepartment(this.value)',
                'style': 'width:200px'
            },
            choices=directorate_list,
        )
        self.fields['department'].widget = forms.Select(
            attrs={
                'id': 'id_department',
                'onchange': 'getDivision(this.value)',
                'style': 'width:200px'
            },
            choices=department_init_form
        )
        self.fields['division'].widget = forms.Select(
            attrs={
                'id': 'id_division',
                'onchange': 'getDivision(this.value)',
                'style': 'width:200px'
            },
            choices=division_init_form
        )
        self.fields['section'].widget = forms.Select(
            attrs={
                'id': 'id_section',
                'style': 'width:200px'
            },
            choices=section_init_form
        )
