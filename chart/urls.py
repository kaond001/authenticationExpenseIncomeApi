from django.urls import path
from . import views


urlpatterns = [
    path('expense_category_summary/', views.ExpenseSummaryStats.as_view(),
         name="statistics"),
    path('income_source_summary/', views.IncomeSummaryStats.as_view(),
         name="statistics"),
]
