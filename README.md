# -cloudfide_task
# Virtual Column Function

A Python function that adds a calculated column to a pandas DataFrame using a simple expression like "quantity * price" as input.
It extracts the two column names and the operator, validates them, and performs the calculation.
Supports `+`, `-` and `*` between two numeric columns. Invalid input returns an empty DataFrame. Original DataFrame is not changed.

A useful feature is that it handles expressions with or without spaces and calculates the whole column at once, without looping through rows. 

## Example

```python
from solution import add_virtual_column

result = add_virtual_column(df, "apples + bananas", "total_fruit")
  apples  bananas  total_fruit
      10        7           17
      12        4           16
       3       14           17
       5        6           11
```

## Task and tests
Task and tests were provided by Cloudfide. 
