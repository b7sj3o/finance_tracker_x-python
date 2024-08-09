from django.contrib import admin
from .models import User, Expense, Income, ExpenseType, IncomeType

admin.site.register(User)
admin.site.register(Expense)
admin.site.register(Income)
admin.site.register(ExpenseType)
admin.site.register(IncomeType)
