from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    username = models.CharField(max_length=50, verbose_name="Нікнейм користувача", unique=True)
    balance = models.IntegerField(verbose_name="Поточний баланс", default=0)
    limit_balance = models.IntegerField(verbose_name="Недоторканний запас", default=0)

    USERNAME_FIELD = 'username'
    
    def __str__(self):
        return self.username
    
    
    def total_expenses(self):
        return sum(x.amount for x in self.expense_set.all())
    
    
    def total_incomes(self):
        return sum(x.amount for x in self.income_set.all())


class Expense(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(verbose_name="Сума")
    expense_type = models.ForeignKey("ExpenseType", on_delete=models.CASCADE, verbose_name="Тип витрати")
    time = models.DateField(default=timezone.now, verbose_name="Час")
    
    def __str__(self):
        return f"{self.amount} - {self.expense_type}"
    

class ExpenseType(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Income(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(verbose_name="Сума")
    income_type = models.ForeignKey("IncomeType", on_delete=models.CASCADE)
    time = models.DateField(default=timezone.now)
    
    def __str__(self):
        return f"{self.amount} - {self.income_type}"
    

class IncomeType(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name