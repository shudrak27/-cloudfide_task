# -cloudfide_task
# Virtual Column

A Python function that adds a calculated column to a pandas DataFrame.

Supports `+`, `-` and `*` between two numeric columns. Invalid input returns an empty DataFrame. Original DataFrame is not changed.

## Example

```python
from solution import add_virtual_column

result = add_virtual_column(df, "apples * bananas", "total_sum")
```

## Task and tests

Task and tests were provided by Cloudfide. 
