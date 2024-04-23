from . import models
from django import forms


class LeaveForm(forms.ModelForm):
    class Meta:
        model = models.Leave
        fields = ["title", "user", "to_date", "from_date", "description"]
