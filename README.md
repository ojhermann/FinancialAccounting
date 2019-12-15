# FinancialAccounting
Financial Accounting with Python

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
 - contains classes used to make entries
 - `Entry` is extended by the two principal classes are `Debit` and `Credit`
   - `account`: `Asset`, `Liability`, or `Equity`, which are extensions of `Account`
   - `key`: a string identifier of the entry
   - `values`: a positive `float` value representing the magnitude of the `Entry`
   - `date`: a `datetime` object
     - defaults to `datetime.now()` 
 