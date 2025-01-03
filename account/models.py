from django.db import models
from organization.models import OrganizationModel


class AccountModel(models.Model):
    id = models.AutoField(primary_key=True)
    organization_id = models.ForeignKey(OrganizationModel, on_delete=models.CASCADE, related_name='organization')
    account_type = models.CharField(max_length=50,)
    account_name = models.CharField(max_length=255)
    team_leader_id = models.IntegerField()
    language = models.CharField(max_length=50, default='en')
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.account_name}"

    class Meta:
        db_table = 'account_detail'


