from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from ..models import Income, IncomeType
from ..forms import IncomeForm, IncomeTypeForm
from .settings import SettingsView


@login_required
def incomes(request):
    incomes = Income.objects.all().order_by('-amount')
    
    if request.method == "POST":
        form = IncomeForm(request.POST)
        
        if form.is_valid():
            amount = form.cleaned_data["amount"]
            income_type = form.cleaned_data["income_type"]
            time = form.cleaned_data["time"]
            
            Income.objects.create(
                creator=request.user,
                amount=amount,
                income_type=income_type,
                time=time,
            )
            SettingsView().update_balance(request)
            
        return redirect("incomes")
    else:
        incomes_form = IncomeForm()
        income_type_form = IncomeTypeForm()
            


    context = {
        "incomes": incomes,
        "incomes_form": incomes_form,
        "incomes_type_form": income_type_form,
    }
    return render(request, 'incomes.html', context)    


@login_required
def create_incomes_type(request):
    if request.method == "POST":
        form = IncomeTypeForm(request.POST)
        
        if form.is_valid():
            IncomeType.objects.create(
                creator=request.user,
                name=form.cleaned_data['name']
            )
    
    return redirect("incomes")


@login_required
def update_income(request, pk):
    income = get_object_or_404(Income, id=pk)
    form = IncomeForm(instance=income)
    
    if request.method == "POST":
        form = IncomeForm(request.POST, instance=income)
        
        if form.is_valid():
            form.save()
            
        return redirect('incomes')
    
    context = {
        "form": form,
        "is_update": True
    }
    
    return render(request, "incomes.html", context)


@login_required
def remove_income(request, pk):
    income = get_object_or_404(Income, id=pk)
    try:
        income.delete()
    except Exception as ex:
        messages.error(request, f"Трапилася помилка: {ex}")
    
    return redirect("incomes")