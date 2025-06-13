from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class inventoryItem(models.Model):
    name=models.CharField(max_length=225)
    quantity=models.IntegerField()
    price=models.FloatField(default=0)
    category=models.ForeignKey('category',on_delete=models.SET_NULL,blank=True,null=True)
    date=models.DateTimeField(auto_now=True)
    user=models.CharField(max_length=225,default='admin')


    def __str__(self):
        return self.name

class category(models.Model):
    name=models.CharField(max_length=225)

    def __str__(self):
        return self.name

class patient_log(models.Model):
    name=models.CharField(max_length=225)
    type = models.ForeignKey('type', on_delete=models.SET_NULL, blank=True, null=True)
    breed=models.CharField(max_length=225)
    category=models.ForeignKey('treatement_category',on_delete=models.SET_NULL,blank=True,null=True)
    date=models.DateTimeField()
    doctor=models.CharField(max_length=225,default='hp')



    def __str__(self):
        return self.name

    def clean(self):
        if self.date is None:
            return
        if self.date <= timezone.now():
            raise ValidationError("Date must be in the future.")

        if patient_log.objects.filter(date=self.date, doctor=self.doctor).exclude(id=self.id).exists():
            raise ValidationError(f"Doctor '{self.doctor}' already has an appointment at this time.")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['doctor', 'date'], name='unique_doctor_appointment_time')
        ]

class treatement_category(models.Model):
    name=models.CharField(max_length=225)

    def __str__(self):
        return self.name

class type(models.Model):
    name=models.CharField(max_length=225)

    def __str__(self):
        return self.name