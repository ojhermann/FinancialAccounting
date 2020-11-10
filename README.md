# FinancialAccounting
Financial Accounting with Python

I've forgotten a lot of financial accounting, so I build this as I revisit the material.

## accounts
- contains classes used to identify an account
- `Account` is extended by three principal classes: `Asset`, `Liability`, and `Equity`
  - these classes should be extended as required, for example:
```python
        class AccountsReceivable(Asset):
            pass

        class AccountsPayable(Liability):
            pass

        class RetainedEarnings(Equity):
            pass
```

## entries
- contains classes used to model a bookkeeping entry
- `Entry` is extended by two principal classes: `Debit` and `Credit`


## transactions
- contains classes used to model bookkeeping transactions
- each `Transaction` object should contain a enough `Debit` and `Credit` objects to balance
