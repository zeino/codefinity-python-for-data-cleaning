import pandas as pd

def drop_missing_rows(df):
    dfCopy = df.copy()
    return dfCopy.dropna()

# Sample DataFrame for testing
import numpy as np
data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, np.nan, 30, 22],
    "city": ["New York", "Los Angeles", np.nan, "Chicago"]
}
df = pd.DataFrame(data)
result = drop_missing_rows(df)
print(result)
