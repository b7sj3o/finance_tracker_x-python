from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Sum

from dataclasses import dataclass

from ..models import Expense, Income


class Home(View):
    incomes = Income.objects.aggregate(Sum("amount"))["amount__sum"]
    expenses = Expense.objects.aggregate(Sum("amount"))["amount__sum"]
    limit_balance = 0

    def get(self, request):
        self.incomes = self.request.user.total_incomes()
        self.expenses = self.request.user.total_expenses()
        self.balance = self.request.user.balance
        self.limit_balance = self.request.user.limit_balance
        
        context = {
            "balance": self.balance,
            "all_incomes": self.incomes,
            "all_expenses": self.expenses,
            "limit_balance": self.limit_balance,
        }
        
        return render(request, "index.html", context)
    
    
    