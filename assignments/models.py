from django.db import models


class AssignDesign (models.Model):

    class Field (models.TextChoices):
        PRODUCT = 'PD', _('Product')

    field = models.CharField (max_length=2, choices= Field.choices)
    value = models.CharField(max_length=50)
    remarks = models.CharField (max_length=100, null=True, blank=True)

    def __str__(self):
        return self.field + ":" + self.value

    class Meta:
        unique_together = [['field','value']]

class Project (models.Model):
    projName = models.CharField (max_length=50)
    product = models.ForeignKey (
        'AssignDesign',
        limit_choices_to={'field':'PD'},
        related_name='prod_name',
        on_delete=models.PROTECT,
        null=True
    startDate = models.DateField()
    endDate = models.DateField()

class Allocation (models.Model):
    project = models.ForeignKey (
        'Project'
    )
