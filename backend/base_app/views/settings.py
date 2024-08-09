from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View


class SettingsView(View):
    template_name = "settings.html"
    
    def get(self, request):
        context = {}
        return render(request, self.template_name, context)

    def post(self, request):
        if request.POST.get("limit_balance"):
            return self.change_limit_balance(request)
        # elif request.POST.get("") TODO: Write some additional functions 
        
        return redirect('settings')
    
    def change_limit_balance(self, request):
        limit_balance = request.POST.get("limit_balance")
        
        try:
            limit_balance = int(limit_balance)
        except:
            messages.error(request, "Неправильний тип даних")
            return redirect('settings')
            
        if limit_balance < 0:
            messages.error(request, "Недоторканний запас не може бути менший нуля")
        elif limit_balance > request.user.balance:
            messages.error(request, "Недоторканний запас не може бути більшим за ваш баланс")
        else:
            request.user.limit_balance = limit_balance
            request.user.save()
            messages.success(request, "Недоторканний запас успішно змінено.")
        
        return redirect("settings")

    def update_balance(self, request):
        balance = request.user.total_incomes() - request.user.total_expenses() 
        
        request.user.balance = balance
        request.user.save()
        messages.success(request, "Баланс успішно оновлено.")