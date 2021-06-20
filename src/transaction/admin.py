from django.contrib import admin
from .models import (
    User, Transaction,
)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total', 'status')
