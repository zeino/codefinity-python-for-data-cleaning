import pandas as pd

def standardize_column_lowercase(df, column_name):
    dfcopy = df.copy()
    dfcopy[column_name] = dfcopy[column_name].str.lower()
    return dfcopy

data = {
    "fruit": ["Apple", "banana", "ORANGE", "apple", "Banana", "orange"],
    "quantity": [5, 3, 4, 2, 1, 6]
}
df = pd.DataFrame(data)
result = standardize_column_lowercase(df, "fruit")
print(result)
