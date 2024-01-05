import pytest
from unittest.mock import MagicMock
from netbanking import NetBankingApp
import tkinter as tk

# Mocking the messagebox.showinfo method
@pytest.fixture
def mock_showinfo(monkeypatch):
    mock = MagicMock()
    monkeypatch.setattr("tkinter.messagebox.showinfo", mock)
    return mock

def test_initial_balance():
    app = NetBankingApp()
    assert app.bank_account.get_balance() == 0

def test_deposit(mock_showinfo):
    app = NetBankingApp()
    app.amount_entry.insert(0, "100")
    
    # Add print statements for debugging
    print("Before perform_transaction:", app.bank_account.get_balance())
    
    app.perform_transaction("Deposit")
    
    # Add print statements for debugging
    print("After perform_transaction:", app.bank_account.get_balance())
    
    assert app.bank_account.get_balance() == 100
    mock_showinfo.assert_called_once_with("Current Balance", "Your current balance is Rs. 100.00")


def test_withdraw_insufficient_balance(mock_showinfo):
    app = NetBankingApp()
    app.amount_entry.insert(0, "100")
    app.perform_transaction("Withdraw")
    assert app.bank_account.get_balance() == 0
    mock_showinfo.assert_called_once_with("Insufficient Balance", "You do not have sufficient balance.")

def test_withdraw_sufficient_balance(mock_showinfo):
    app = NetBankingApp()
    app.amount_entry.insert(0, "50")
    app.perform_transaction("Deposit")
    app.amount_entry.delete(0, tk.END)
    app.amount_entry.insert(0, "30")
    app.perform_transaction("Withdraw")
    assert app.bank_account.get_balance() == 20
    mock_showinfo.assert_called_once_with("Current Balance", "Your current balance is Rs. 20.00")

if __name__ == "__main__":
    pytest.main()
