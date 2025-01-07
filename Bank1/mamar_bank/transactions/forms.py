from typing import Any
from django import forms
from .models import Transactions
from accounts.models import UserBankAccount


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ['amount', 'transaction_type']

    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('account')
        super().__init__(*args, **kwargs)
        self.fields['transaction_type'].disabled = True
        self.fields['transaction_type'].widget = forms.HiddenInput()

    def save(self, commit=True):
        self.instance.account = self.account
        self.instance.balance_after_transaction = self.account.balance
        return super().save()


class SendMoneyForm(TransactionForm):
    account_no = forms.IntegerField()

    class Meta:
        model = Transactions
        fields = ['amount', 'transaction_type']

    def clean_account_no(self):
        account_no = self.cleaned_data['account_no']
        account = UserBankAccount.objects.filter(
            account_no=account_no).exists()
        if not account:
            raise forms.ValidationError(
                f"User with account {account_no} does not exist")
        return account_no

    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount > self.account.balance:
            raise forms.ValidationError(f"You don't have enough money")
        return amount


class DepositForm(TransactionForm):
    def clean_amount(self):
        min_deposit = 100
        amount = self.cleaned_data.get('amount')
        if amount < min_deposit:
            raise forms.ValidationError(
                f"Minimum deposit amount is {min_deposit}"
            )
        return amount


class WithdrawalForm(TransactionForm):
    def clean_amount(self):
        account = self.account
        min_withdraw_amount = 500
        max_withdraw_amount = 20000
        balance = account.balance # 1000
        amount = self.cleaned_data.get('amount')
        if amount < min_withdraw_amount:
            raise forms.ValidationError(
                f'You can withdraw at least {min_withdraw_amount} $'
            )

        if amount > max_withdraw_amount:
            raise forms.ValidationError(
                f'You can withdraw at most {max_withdraw_amount} $'
            )

        if amount > balance: 
            raise forms.ValidationError(
                f'You have {balance} $ in your account. '
                'You can not withdraw more than your account balance'
            )

        return amount


class LoanRequestForm(TransactionForm):
    def clean_amount(self):
        amount = self.cleaned_data["amount"]
        return amount