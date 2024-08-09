from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from ..models import Expense, ExpenseType
from ..forms import ExpenseForm, ExpenseTypeForm
from .settings import SettingsView


def expenses(request):
    expenses = Expense.objects.filter(creator=request.user).order_by('amount')
    
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        
        if form.is_valid():
            amount = int(form.cleaned_data["amount"])
            expense_type = form.cleaned_data["expense_type"]
            time = form.cleaned_data["time"]
            use_limit_balance = form.cleaned_data["use_limit_balance"]
            
            if request.user.balance >= amount:
                if (request.user.balance - request.user.limit_balance >= amount) or use_limit_balance:
                    Expense.objects.create(
                        creator=request.user,
                        amount=amount,
                        expense_type=expense_type,
                        time=time,
                    )
                    SettingsView().update_balance(request)
                else:
                    messages.error(request, "На вашому балансі недостатньо коштів, але буде достатньо з НЗ")
                
            else:
                messages.error(request, "На вашому балансі недостатньо коштів")
            
        return redirect("expenses")
    else:
        expense_form = ExpenseForm()
        expense_type_form = ExpenseTypeForm()
            
    context = {
        "expenses": expenses,
        "expenses_form": expense_form,
        "expenses_type_form": expense_type_form,
    }
    return render(request, 'expenses.html', context)   


def create_expenses_type(request):
    if request.method == "POST":
        form = ExpenseTypeForm(request.POST)
        
        if form.is_valid():
            ExpenseType.objects.create(
                creator=request.user,
                name=form.cleaned_data['name']
            )
    
    return redirect("expenses")


def update_expense(request, pk):
    expense = get_object_or_404(Expense, id=pk)
    form = ExpenseForm(instance=expense)
    
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        
        if form.is_valid():
            form.save()
        return redirect('expenses')
    
    context = {
        "form": form,
        "is_update": True
    }
    
    return render(request, "expenses.html", context)


def remove_expense(request, pk):
    expense = get_object_or_404(Expense, id=pk)
    try:
        expense.delete()
    except Exception as ex:
        messages.error(request, f"Трапилася помилка: {ex}")
    
    return redirect("expenses")