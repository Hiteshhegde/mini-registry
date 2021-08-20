from django.db import models

# Create your models here.
class DomainName(models.Model):
    domain_name = models.CharField(max_length=36)
    period_of_reg = models.DurationField()
    verified_contact = models.TextField(null=True)

    
     