from django.contrib import admin
from tracker.models import *

admin.site.site_header= "Expense Tracker"
admin.site.site_title= "Expense Tracker"
admin.site.site_url= "expense-tracker"

admin.site.register(CurrentBalance)

@admin.action(description= "Mark selected expenses as Credit")
def make_credit(modeladmin, request, queryset):
    queryset.update(expense_type="CREDIT")

@admin.action(description= "Mark selected expenses as Debit")
def make_debit(modeladmin, request, queryset):
    queryset.update(expense_type="DEBIT")

class TrackingHistoryAdmin(admin.ModelAdmin):
    list_display=[
    "amount",
    "expense_type",
    "description",
    "created_at",
    "display_age"

    ]

    actions=[make_credit, make_debit]

    def display_age(self, obj):
        if obj.amount>0:
            return "positive"
        else:
            return "negative"

    search_fields= ["expense_type", "description", "amount"]
    ordering=["expense_type"]
    list_filter=["expense_type"]

admin.site.register(TrackingHistory, TrackingHistoryAdmin)