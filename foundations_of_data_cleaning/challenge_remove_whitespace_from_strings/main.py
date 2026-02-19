import pandas as pd

def strip_whitespace(df):
    text_cols = df.select_dtypes(include="object").columns
    cleaned = df[text_cols].apply(lambda col: col.str.strip())
    df[text_cols] = cleaned
                                
    return df

data = {
    "Fruit": [" apple", "banana ", "  cherry ", "date"],
    "Color": [" red", "yellow ", " red ", "brown"],
    "Count": [10, 5, 7, 3]
}

df = pd.DataFrame(data)
cleaned_df = strip_whitespace(df)
print(cleaned_df)
