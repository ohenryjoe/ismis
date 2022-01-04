from django.db import models
from django.db.models import ForeignKey

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Male'),
    ('B', 'Both'),
]

MARITAL_CHOICES = [
    ('M', 'Married'),
    ('S', 'Single'),
    ('W', 'Widowed'),
    ('D', 'Divorced'),
]

TITLE_CHOICES = [
    ('Mr', 'Mister'),
    ('Ms', 'Miss'),
    ('Mrs', 'Mrs'),
    ('Dr.', 'Doctor'),
    ('Eng.', 'Engineer'),
    ('Prof.', 'Professor'),
    ('Hon.', 'Honourable'),
]

NATIONALITY_CHOICES = [
    ('Uganda', 'Uganda'),
    ('Kenya', 'Kenya'),
    ('Rwanda', 'Rwanda'),
    ('South Sudan', 'South Sudan'),
    ('Burundi', 'Burundi'),
    ('Tanzania', 'Tanzania'),
    ('Non EAC Country', 'Non EAC Country'),
]

MONTHS = [
    ('Jan', 'January'),
    ('Feb', 'February'),
    ('Mar', 'March'),
    ('Apr', 'April'),
    ('May', 'May'),
    ('Jun', 'June'),
    ('July', 'July'),
    ('Aug', 'August'),
    ('sept', 'September'),
    ('Oct', 'October'),
    ('Nov', 'November'),
    ('Dec', 'December'),
]
DAY_CHOICES = [
    ('01', '1st'),
    ('02', '2nd'),
    ('03', '3rd'),
    ('04', '4th'),
    ('05', '5th'),
    ('06', '6th'),
    ('07', '7th'),
    ('08', '8th'),
    ('09', '9th'),
    ('10', '10th'),
    ('11', '11th'),
    ('12', '12th'),
    ('13', '13th'),
    ('14', '14th'),
    ('15', '15th'),
    ('16', '16th'),
    ('17', '17th'),
    ('18', '18th'),
    ('19', '19th'),
    ('20', '20th'),
    ('21', '21st'),
    ('22', '22nd'),
    ('23', '23th'),
    ('24', '24th'),
    ('25', '25th'),
    ('26', '26th'),
    ('27', '27th'),
    ('28', '28th'),
    ('29', '29th'),
    ('30', '30th'),
    ('31', '31st'),
]

# Give different name to the levels (like alias)


class EntityLevel(models.Model):
    # Determine the chain in corporate structure [Level 1, Level 2]
    rank = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    default_parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
    active = models.BooleanField()
    created_by = models.PositiveBigIntegerField(blank=True, null=True)
    updated_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'levels'

    def __str__(self):
        return self.name


class CorporateEntity(models.Model):
    # Determine the chain in corporate structure [CEO -> Level 1(Entity), Directorate -> Level 2(Entity)] [Both are groups]
    level = models.ForeignKey(EntityLevel, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField()
    created_by = models.PositiveSmallIntegerField(blank=True, null=True)
    updated_by = models.PositiveSmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = 'entities'

    def __str__(self):
        return self.title


class Directorates(models.Model):
    # Alternate method (Corporate division above departments)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField()
    created_by = models.PositiveSmallIntegerField(blank=True, null=True)
    updated_by = models.PositiveSmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = 'directorates'

    def __str__(self):
        return self.title


class Departments(models.Model):
    # alternate
    directorate = models.ForeignKey(Directorates, blank=True, null=True, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField()
    created_by = models.PositiveSmallIntegerField(blank=True, null=True)
    updated_by = models.PositiveSmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = 'departments'

    def __str__(self):
        return self.title


class Divisions(models.Model):
    # alternate
    directorate = models.ForeignKey(Directorates, blank=True, null=True, on_delete=models.DO_NOTHING)
    department = models.ForeignKey(Departments, blank=True, null=True, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_by = models.PositiveSmallIntegerField(blank=True, null=True)
    updated_by = models.PositiveSmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = 'divisions'


class Sections(models.Model):
    # alternate
    directorate = models.ForeignKey(Directorates, blank=True, null=True, on_delete=models.DO_NOTHING)
    department = models.ForeignKey(Departments, blank=True, null=True, on_delete=models.DO_NOTHING)
    division = models.ForeignKey(Divisions, blank=True, null=True, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_by = models.PositiveBigIntegerField(blank=True, null=True)
    updated_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'sections'

    def __str__(self):
        return self.title


class SalaryScales(models.Model):
    scale = models.CharField(max_length=255)
    rank_order = models.PositiveIntegerField()  # e.g 1, 2, 3 etc the smaller, the more senior # unique as well
    heads = models.ForeignKey(EntityLevel, blank=True, null=True,
                              on_delete=models.SET_NULL)  # e.g 1, 2, 3 etc level id headed by salary scale
    # Salary scale bound to a designation
    rank_title = models.CharField()  # e.g Principal Officer
    rank_description = models.TextField(blank=True, null=True)  # e.g Heads a Section
    created_by = models.PositiveSmallIntegerField(blank=True, null=True)
    updated_by = models.PositiveSmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = 'salary_scales'

    def __str__(self):
        return self.scale


class Designations(models.Model):
    title = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255, blank=True, null=True)
    
    # Where a job is placed might not always be sections
    directorate = models.ForeignKey(Directorates, blank=True, null=True, on_delete=models.CASCADE,related_name='designation_directorate',)
    department = models.ForeignKey(Departments, blank=True, null=True, on_delete=models.CASCADE,related_name='designation_department')
    division = models.ForeignKey(Divisions, blank=True, null=True, on_delete=models.CASCADE,related_name='designation_division')
    section = models.ForeignKey(Sections, blank=True, null=True, on_delete=models.CASCADE,related_name='designation_section')
    
    salary_scale = models.ForeignKey(SalaryScales, on_delete=models.CASCADE)
    supervisor = models.ForeignKey('self', on_delete=models.CASCADE)
    probational = models.BooleanField()
    probation_period = models.PositiveIntegerField(blank=True, null=True)
    job_summary = models.TextField(blank=True, null=True)
    job_description = models.TextField(blank=True, null=True)
    max_holders = models.IntegerField()
    active = models.BooleanField()
    
    headed_entity = models.ForeignKey(EntityLevel, blank=True, null=True,
                                      on_delete=models.SET_NULL)  # the id of headed entity
    created_by = models.PositiveSmallIntegerField(blank=True, null=True)
    updated_by = models.PositiveSmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = 'designations'

    def __str__(self):
        return self.title

    def get_designations(self):
        drt = self.directorate
        dep = self.department
        div = self.division
        sec = self.section
        if sec:
            Desig = Designations.objects.filter(section=sec)
        elif div:
            Desig = Designations.objects.filter(division=div)
        elif dep:
            Desig = Designations.objects.filter(department=dep)
        elif dir:
            Desig = Designations.objects.filter(directorate=drt)
        else:
            Desig = Designations.objects.get(designations__salary_scale__rank_order=1)
        return Desig


class Titles(models.Model):
    # We can get it with constant
    title = models.CharField(max_length=50,
                             choices=TITLE_CHOICES,
                             default="Mr")
    created_by = models.PositiveBigIntegerField(blank=True, null=True)
    updated_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'titles'

    def __str__(self):
        return self.title + '. '


class Genders(models.Model):    # We can get it with constant
    title = models.CharField(max_length=255)
    created_by = models.PositiveBigIntegerField(blank=True, null=True)
    updated_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'genders'

    def __str__(self):
        return self.title


class Addressable(models.Model):
    # adreess fields needed
    model_name = models.CharField(max_length=255)
    created_by = models.PositiveBigIntegerField(blank=True, null=True)
    updated_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'addressables'


class Contactable(models.Model):
    # Same model for the address
    model_name = models.CharField(max_length=255)
    created_by = models.PositiveBigIntegerField(blank=True, null=True)
    updated_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'contactables'


class Commentable(models.Model):
    # Same as address
    model_name = models.CharField(max_length=255)
    created_by = models.PositiveBigIntegerField(blank=True, null=True)
    updated_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'commentables'


class EmploymentStatuses(models.Model):
    # Special Neeeds Employees ['Active', 'Retired']
    # current_status = 'retire' in Employee model
    # Logs

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'employee_statuses'


class EmployeeSNEStatuses(models.Model):
    
    # Special Neeeds Employees ['Blind', 'Physically Handicapped']
    code = models.CharField(max_length=4)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'employee_sne_statuses'

    def __str__(self):
        return self.title


class EmploymentTenure(models.Model):
    # Contract, Permanent e.t.c
    code = models.CharField(max_length=4)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'employment_terms'

    def __str__(self):
        return self.title


class EmploymentTypes(models.Model):  # includes part-time, full-time etc
    code = models.CharField(max_length=4)
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'employment_types'

    def __str__(self):
        return self.title


class Religions(models.Model):
    title = models.CharField(max_length=255)
    created_by = models.PositiveBigIntegerField(blank=True, null=True)
    updated_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'religions'

    def __str__(self):
        return self.title


class Employees(models.Model):
    employee_number = models.CharField(unique=True, max_length=10)
    username = models.CharField(unique=True, max_length=255)
    title = models.CharField(max_length=50,
                             choices=TITLE_CHOICES,
                             default="Mr")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.ForeignKey(Genders, blank=True, null=True, on_delete=models.SET_NULL)
    nationality = models.CharField(max_length=50,
                                   choices=NATIONALITY_CHOICES,
                                   default="Uganda")
    marital_status = models.CharField(max_length=50,
                                      choices=MARITAL_CHOICES,
                                      default="Uganda")
    religion = ForeignKey(Religions, blank=True, null=True, on_delete=models.CASCADE)
    email = models.CharField(max_length=255, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    nin = models.CharField(max_length=14, default='12345678912345')
    passport = models.CharField(max_length=10, blank=True, null=True)
    nssf = models.CharField(max_length=14, blank=True, null=True)
    tin = models.CharField(max_length=12, blank=True, null=True)
    permit = models.CharField(max_length=12, blank=True, null=True)
    date_joined = models.DateField(blank=True, null=True)
    avatar = models.FileField()
    designation = models.ForeignKey(Designations, blank=True, null=True, on_delete=models.CASCADE)
    salary_scale = models.ForeignKey(SalaryScales, blank=True, null=True, on_delete=models.CASCADE)
    exit_date = models.DateField(blank=True, null=True)
    employee_sne_status = models.ForeignKey(EmployeeSNEStatuses, blank=True, null=True, on_delete=models.CASCADE)
    employment_status = models.ForeignKey(EmploymentStatuses, blank=True, null=True, on_delete=models.CASCADE)
    employment_term = models.ForeignKey(EmploymentTenure, blank=True, null=True, on_delete=models.CASCADE)
    employment_type = models.ForeignKey(EmploymentTypes, blank=True, null=True, on_delete=models.CASCADE)
    created_by = models.PositiveBigIntegerField(blank=True, null=True)
    approved_by = models.PositiveBigIntegerField(blank=True, null=True)
    approved_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    other_names = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'employees'

    def __str__(self):
        return self.get_full_name

    def get_full_name(self):
        full_name = self.title.capitalize() + '. ' \
                    + self.first_name.capitalize() + ' ' \
                    + self.middle_name.capitalize() + ' ' \
                    + self.last_name.capitalize()
        return full_name


class Addresses(models.Model):
    class address_types(models.TextChoices):
        PERMANENT = 'P', 'Personal'
        RESIDENCE = 'H', 'Home'
        WORK = 'W', 'Work'
        
    country = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    subregion = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    subcounty = models.CharField(max_length=255)
    parish = models.CharField(max_length=255)
    village = models.CharField(max_length=255)
    street = models.CharField(max_length=255, blank=True, null=True)
    plot = models.CharField(max_length=255, blank=True, null=True)
    building_name = models.CharField(max_length=255, blank=True, null=True)
    floor = models.CharField(max_length=255, blank=True, null=True)
    room = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=2, choices=address_types.choices, default=address_types.WORK, )
    created_by = models.PositiveBigIntegerField(blank=True, null=True)
    updated_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'addresses'


class EmployeeBanks(models.Model):
    id = models.BigAutoField(primary_key=True)
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=255)
    bank_branch = models.CharField(max_length=255)
    account_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=255)
    swift_code = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.PositiveBigIntegerField(blank=True, null=True)
    updated_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'employee_banks'

    def __str__(self):
        return self.bank_name

    
# RelatedPerson Table that consist of information related to related person


class Contacts(models.Model):
    employee = models.ForeignKey(Employee)
    contactable_type = models.ForeignKey(RelationShip) # spouse, myself, parents
    value = models.CharField(max_length=255)
    kind = models.CharField(max_length=9)
    type = models.CharField(max_length=8)
    created_by = models.PositiveBigIntegerField(blank=True, null=True)
    updated_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'contacts'


class Delegations(models.Model):
    # Work Delegations
    substantive = models.PositiveBigIntegerField()
    delegated = models.PositiveBigIntegerField()
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    permissions = models.TextField(blank=True, null=True)
    active = models.BooleanField()
    created_by = models.PositiveBigIntegerField(blank=True, null=True)
    updated_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'delegations'


class Relationships(models.Model):
    # Spouse, Father, Brother
    title = models.CharField(max_length=255)
    created_by = models.PositiveBigIntegerField(blank=True, null=True)
    updated_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'relationships'

    def __str__(self):
        return self.title


class DocumentTypes(models.Model):
    # 
    title = models.CharField(max_length=255)
    category = models.ForeignKey(DocumentCategories, on_delete=models.CASCADE)
    created_by = models.PositiveBigIntegerField(blank=True, null=True)
    updated_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'document_types'

    def __str__(self):
        return self.title


class Documents(models.Model):
    employee = models.ForeignKey(Employees, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    size = float()
    description = models.TextField(blank=True, null=True)
    path = models.CharField(max_length=255, blank=True, null=True)
    document_category = models.ForeignKey(DocumentCategories, on_delete=models.DO_NOTHING)
    document_type = models.ForeignKey(DocumentTypes, on_delete=models.DO_NOTHING)
    created_by = models.PositiveBigIntegerField(blank=True, null=True)
    updated_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'documents'

    def __str__(self):
        return self.title


class Educations(models.Model):
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    institution = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_month = models.CharField(max_length=12, choices=MONTHS, default='January', )
    start_year = models.CharField(max_length=4)
    end_month = models.CharField(max_length=12, choices=MONTHS, default='January', )
    end_year = models.CharField(max_length=4)
    certificate_path = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.PositiveBigIntegerField(blank=True, null=True)
    updated_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'educations'


class EmploymentHistory(models.Model):
    action = models.CharField(max_length=255)
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    from_designation = models.PositiveBigIntegerField(blank=True, null=True)
    to_designation = models.PositiveBigIntegerField(blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    created_by = models.PositiveBigIntegerField(blank=True, null=True)
    updated_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'employment_history'


class Experiences(models.Model):
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    description = models.TextField()
    start_month = models.CharField(max_length=12, choices=MONTHS, default='January', )
    start_year = models.CharField(max_length=4)
    end_month = models.CharField(max_length=12, choices=MONTHS, default='January', )
    end_year = models.CharField(max_length=4)
    recommendation_path = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.PositiveBigIntegerField(blank=True, null=True)
    updated_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'experiences'


class LeaveApplicationSettings(models.Model):
    designation = models.OneToOneField(Designations, unique=True, on_delete=models.CASCADE)
    verified_by = models.OneToOneField(Designations, related_name='verifier', on_delete=models.CASCADE)
    approved_by = models.ForeignKey(Designations, related_name='approver', on_delete=models.CASCADE)
    granted_by = models.ForeignKey(Designations, related_name='granter', on_delete=models.CASCADE)
    updated_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'leave_application_settings'


class LeaveApplicationStatuses(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'leave_application_statuses'

    def __str__(self):
        return self.name


class LeaveApplications(models.Model):
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    leave_type = models.PositiveBigIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.PositiveIntegerField()
    status = models.ForeignKey(LeaveApplicationStatuses, default=1, on_delete=models.SET_DEFAULT)
    created_by = models.PositiveBigIntegerField(blank=True, null=True)
    updated_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'leave_applications'


class LeaveTypes(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    active = models.IntegerField()
    created_by = models.PositiveBigIntegerField(blank=True, null=True)
    updated_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'leave_types'

    def __str__(self):
        return self.name


class LeavePolicies(models.Model):
    leave_type = models.ForeignKey(LeaveTypes, on_delete=models.CASCADE)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default=GENDER_CHOICES.__getitem__(0), )
    duration = models.PositiveIntegerField()
    with_weekend = models.BooleanField()
    earned_leave = models.BooleanField()
    carry_forward = models.BooleanField()
    max_carry_forward_duration = models.PositiveIntegerField(blank=True, null=True)
    policyname = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    active = models.IntegerField()
    created_by = models.PositiveBigIntegerField(blank=True, null=True)
    updated_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'leave_policies'


class Leaves(models.Model):
    application = ForeignKey(LeaveApplications, on_delete=models.CASCADE)
    leave_type = ForeignKey(LeaveTypes, on_delete=models.CASCADE)
    employee = ForeignKey(Employees, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=9)
    created_by = models.PositiveBigIntegerField(blank=True, null=True)
    updated_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'leaves'


class LeaveBalances(models.Model):
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    leave_type = ForeignKey(LeaveTypes, on_delete=models.CASCADE)
    policy = models.ForeignKey(LeavePolicies, on_delete=models.CASCADE)
    join_date = models.DateField()
    leave_start_date = models.DateField()
    leave_end_date = models.DateField()
    entitlement = models.PositiveIntegerField(blank=True, null=True)
    days_taken = models.PositiveIntegerField(blank=True, null=True)
    balance = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.PositiveBigIntegerField(blank=True, null=True)
    updated_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'leave_balances'


class LeaveRecalls(models.Model):
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    leave = models.ForeignKey(Leaves, on_delete=models.CASCADE)
    leave_recall_date = models.DateTimeField()
    leave_return_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveBigIntegerField(blank=True, null=True)
    updated_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'leave_recalls'


class LeaveSettings(models.Model):
    leave_type = models.ForeignKey(LeaveTypes, on_delete=models.CASCADE)
    duration = models.PositiveIntegerField()
    with_weekend = models.BooleanField()
    earned_leave = models.BooleanField()
    carry_forward = models.BooleanField()
    max_carry_forward_duration = models.PositiveIntegerField()
    created_by = models.PositiveBigIntegerField(blank=True, null=True)
    updated_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'leave_settings'


class LeaveStatuses(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'leave_statuses'


class LeaveTrackers(models.Model):
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    period_start_date = models.DateField()
    period_end_date = models.DateField()
    leave_type = models.ForeignKey(LeaveTypes, on_delete=models.CASCADE)
    leave_application = models.ForeignKey(LeaveApplications, on_delete=models.CASCADE)
    date_on_leave = models.DateField()
    status = models.CharField(max_length=8)
    created_by = models.PositiveBigIntegerField(blank=True, null=True)
    updated_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'leave_trackers'


class MaritalStatuses(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_by = models.PositiveBigIntegerField(blank=True, null=True)
    updated_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'marital_statuses'


class PolicyScales(models.Model):
    leave_policy = models.PositiveBigIntegerField()
    salary_scale = models.PositiveBigIntegerField()
    active = models.IntegerField()
    created_by = models.PositiveBigIntegerField(blank=True, null=True)
    updated_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'policy_scales'
        unique_together = (('leave_policy', 'salary_scale'),)


class RelatedPersons(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    nin = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True)
    title = models.CharField(max_length=4, blank=True, null=True)
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    relationship = models.ForeignKey(Relationships, on_delete=models.CASCADE)
    emergency = models.BooleanField()
    dependant = models.BooleanField()
    is_next_of_kin = models.BooleanField()
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.PositiveBigIntegerField(blank=True, null=True)
    updated_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'related_persons'


class Resignations(models.Model):
    id = models.BigAutoField(primary_key=True)
    employee = models.PositiveBigIntegerField()
    start_date = models.DateTimeField()
    status = models.CharField(max_length=8)
    approved_at = models.DateTimeField(blank=True, null=True)
    approved_start_date = models.DateTimeField(blank=True, null=True)
    reason = models.TextField()
    comments = models.TextField(blank=True, null=True)
    approved_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_by = models.PositiveBigIntegerField(blank=True, null=True)
    updated_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'resignations'
