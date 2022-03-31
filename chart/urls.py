from django.urls import path
from . import views


urlpatterns = [
    path('', views.ExpenseSummaryStats.as_view(), name="expenses_category_summary"),
]