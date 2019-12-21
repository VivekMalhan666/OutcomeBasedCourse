from django.db import models
import uuid


class Institute(models.Model):
    institute_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    institute_name = models.CharField(max_length=300)

    def __str__(self):
        return self.institute_name


class Level(models.Model):
    """Level can be: U.G., P.G., etc.
    """

    level_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    level_name = models.CharField(max_length=50)
    institute = models.ManyToManyField(Institute, blank=True)

    def __str__(self):
        return self.level_name


class Programme(models.Model):
    programme_code = models.CharField(primary_key=True, max_length=10)
    programme_name = models.CharField(max_length=50)
    programme_fees = models.IntegerField()
    level = models.ForeignKey(
        Level, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return self.programme_name


class Discipline(models.Model):
    discipline_code = models.CharField(primary_key=True, max_length=10)
    discipline_name = models.CharField(max_length=50)
    total_credits = models.DecimalField(max_digits=5, decimal_places=2)
    programme = models.ForeignKey(
        Programme, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return self.discipline_name


class Course(models.Model):
    course_id = models.CharField(primary_key=True, max_length=20)
    course_title = models.CharField(max_length=200)
    course_overview = models.TextField(blank=True, null=True)
    course_outcome = models.TextField(blank=True, null=True)
    course_objective = models.TextField(blank=True, null=True)
    course_credit = models.DecimalField(max_digits=4, decimal_places=2)
    contact_hours_per_week = models.DecimalField(max_digits=4, decimal_places=2)
    course_resources = models.TextField(blank=True, null=True)
    course_test = models.TextField(blank=True, null=True)
    discipline = models.ManyToManyField(Discipline, blank=True)

    def __str__(self):
        return self.course_title


class Module(models.Model):
    module_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    module_title = models.CharField(max_length=200)
    module_overview = models.TextField(blank=True, null=True)
    module_outcome = models.TextField(blank=True, null=True)
    module_objective = models.TextField(blank=True, null=True)
    module_body = models.TextField(blank=True, null=True)
    module_resources = models.TextField(blank=True, null=True)
    module_test = models.TextField(blank=True, null=True)
    course = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return self.module_title


class Unit(models.Model):
    unit_number = models.AutoField(primary_key=True)
    unit_name = models.CharField(max_length=200, blank=True, null=True)
    unit_overview = models.TextField(blank=True, null=True)
    unit_outcome = models.TextField(blank=True, null=True)
    unit_objective = models.TextField(blank=True, null=True)
    unit_body = models.TextField(blank=True, null=True)
    unit_resources = models.TextField(blank=True, null=True)
    unit_test = models.TextField(blank=True, null=True)
    module = models.ManyToManyField(Module, blank=True)

    def __str__(self):
        return (
            "Unit "
            + str(self.unit_number)
            + (". " + self.unit_name if self.unit_name else "")
        )
