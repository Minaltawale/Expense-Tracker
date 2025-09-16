from django.db import models
from django.contrib.auth.models import User

class CurrentBalance(models.Model):
    current_balance= models.FloatField(default=0)

class TrackingHistory(models.Model):
    current_balance= models.ForeignKey(CurrentBalance, on_delete= models.CASCADE)
    amount= models.FloatField(editable= False)
    expense_type= models.CharField(choices= (("CREDIT", "CREDIT"), ("DEBIT", "DEBIT")), max_length= 200)
    description= models.CharField(max_length= 200)
    created_at= models.DateTimeField(auto_now= True)
    updated_at= models.DateTimeField(auto_now_add= True)

    def __str__(self)->str:
        return f"The amount is {self.amount} for {self.description} expense type is {self.expense_type}"