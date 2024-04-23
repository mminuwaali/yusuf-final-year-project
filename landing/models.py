from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

STATUS = [(i, i) for i in ["pending", "rejected", "accepted"]]


class Leave(models.Model):
    to_date = models.DateField()
    from_date = models.DateField()
    description = models.TextField()
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    reason = models.TextField(default="", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="pending", choices=STATUS)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Department(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name.title()
