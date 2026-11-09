import re
import pandas as pd
from pandas.api.types import is_numeric_dtype

#add_virtual_column function
def add_virtual_column(
    df: pd.DataFrame,
    role: str,
    new_column: str,
) -> pd.DataFrame:
    #valiate for input types
    if not isinstance(role, str) or not isinstance(new_column, str) or not isinstance(df, pd.DataFrame):
        return pd.DataFrame()

    #validte column names
    column_pattern = r"[A-Za-z_]+"

    for column in [*df.columns, new_column]:
        if not isinstance(column, str):
            return pd.DataFrame()

        if re.fullmatch(column_pattern, column) is None:
            return pd.DataFrame()

    #validate for duplicates in column names
    if not df.columns.is_unique or new_column in df.columns:
        return pd.DataFrame()

    #take two column names and allowed operator between
    expression_pattern = (
        r"\s*([A-Za-z_]+)\s*([+*-])\s*([A-Za-z_]+)\s*"
    )
    match = re.fullmatch(expression_pattern, role)

    if match is None:
        return pd.DataFrame()

    column_one, operation, column_two = match.groups()

    #validate that both columns exist
    if column_one not in df.columns or column_two not in df.columns:
        return pd.DataFrame()

    left = df[column_one]
    right = df[column_two]

    #check that columns used in calculaton are numeric
    if not is_numeric_dtype(left) or not is_numeric_dtype(right):
        return pd.DataFrame()

    # Calculate the new column.
    if operation == "+":
        calculated = left + right
    elif operation == "-":
        calculated = left - right
    else:
        calculated = left * right

    result = df.copy()
    result[new_column] = calculated

    return result

#function apply

fruit_data = {
    "apples": [10, 12, 3, 5],
    "bananas": [7, 4, 14, 6],
}

fruit_sales = pd.DataFrame(fruit_data)

result = add_virtual_column(
    fruit_sales,
    "apples + bananas",
    "total_fruit",
)

print(result)