from django import forms

from .models import Schedule, Task


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'
        labels = {
            'subject_name': 'Subject Name',
            'subject_code': 'Subject Code',
            'instructor': 'Instructor',
            'day': 'Day',
            'start_time': 'Start Time',
            'end_time': 'End Time',
            'room': 'Room',
        }
        widgets = {
            'subject_name': forms.TextInput(attrs={'class': 'form-control'}),
            'subject_code': forms.TextInput(attrs={'class': 'form-control'}),
            'instructor': forms.TextInput(attrs={'class': 'form-control'}),
            'day': forms.Select(attrs={'class': 'form-select'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'room': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        if start_time and end_time and end_time < start_time:
            raise forms.ValidationError('End time must be later than or equal to the start time.')

        return cleaned_data


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        labels = {
            'task_name': 'Task Name',
            'task_type': 'Type',
            'subject': 'Subject',
            'description': 'Description',
            'deadline': 'Deadline',
        }
        widgets = {
            'task_name': forms.TextInput(attrs={'class': 'form-control'}),
            'task_type': forms.Select(attrs={'class': 'form-select'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'deadline': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
