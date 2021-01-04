from django.db import models
from account.models import User
import uuid

class Transaction(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    created_by = models.ForeignKey(User, on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    trans_from = models.CharField(max_length=128)
    trans_to = models.CharField(max_length=128)
    amount = models.FloatField()
    reason = models.CharField(max_length=128)
    budget_det = models.CharField(max_length=128)