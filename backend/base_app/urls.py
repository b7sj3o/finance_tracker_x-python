from django.urls import path
from . views import (
    Home,
    SettingsView,
    
    login_user,
    register_user,
    logout_user,
    incomes,
    expenses,
    create_expenses_type,
    create_incomes_type,
    update_expense,
    update_income,
    remove_expense,
    remove_income
    
)

urlpatterns = [
    path("", Home.as_view(), name="home"),

    # ---- AUTH ----
    path("login_user", login_user, name="login_user"),
    path("logout_user", logout_user, name="logout_user"),
    path("register_user", register_user, name="register_user"),
    
    # ---- EXPENSES ----
    path("create_expenses_type", create_expenses_type, name="create_expenses_type"),
    path("expenses", expenses, name="expenses"),
    path("update_expense/<int:pk>", update_expense, name="update_expense"),
    path("remove_expense/<int:pk>", remove_expense, name="remove_expense"),
    
    # ---- INCOMES ----
    path("create_incomes_type", create_incomes_type, name="create_incomes_type"),
    path("incomes", incomes, name="incomes"),
    path("update_income/<int:pk>", update_income, name="update_income"),
    path("remove_income/<int:pk>", remove_income, name="remove_income"),
    
    
    # ---- USER SETTINGS ----
    path("settings", SettingsView.as_view(), name="settings"),
    
    
]

