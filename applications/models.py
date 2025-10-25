

# Create your models here.
from django.db import models

class JobApplication(models.Model):
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    application_date = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=50,
        choices=[('Applied', 'Applied'), ('Interview', 'Interview'), ('Rejected', 'Rejected'), ('No Reply', 'No Reply')],
        default='Applied'
    )
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.company_name} - {self.job_title}"
