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
 - contains classes used to make debit or credit entries
 - `Entry` is extended by `Debit` and `Credit`
   - `account`: `Asset`, `Liability`, or `Equity` (see [accounts](#accounts))
   - `identifier`: a string identifier of the entry
   - `currency`: the currency of the entry
   - `value`: a `float` value representing the magnitude of the entry
     - this must be positive
   - `date`: a `datetime` object corresponding the the activity that resulting in the entry
     - defaults to `datetime.utcnow()` 


## transactions
- `Transaction` a class representing a transaction
  - there must be at least one debit and one credit
  - the sum of the value of the debits must equal the sum of the value of credits
