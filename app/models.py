from django.core.exceptions import ValidationError
from django.db import models


class Schedule(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    subject_name = models.CharField(max_length=200)
    subject_code = models.CharField(max_length=50)
    instructor = models.CharField(max_length=200)
    day = models.CharField(max_length=20, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['day', 'start_time']

    def clean(self):
        super().clean()
        if self.start_time and self.end_time and self.end_time < self.start_time:
            raise ValidationError({'end_time': 'End time must be later than or equal to start time.'})

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.subject_name} ({self.subject_code})"


class Task(models.Model):
    TASK_TYPE_CHOICES = [
        ('Assignment', 'Assignment'),
        ('Project', 'Project'),
        ('Activity', 'Activity'),
        ('Other', 'Other'),
    ]

    task_name = models.CharField(max_length=200)
    task_type = models.CharField(max_length=20, choices=TASK_TYPE_CHOICES)
    subject = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['deadline', 'task_name']

    def __str__(self):
        return f"{self.task_name} ({self.task_type})"