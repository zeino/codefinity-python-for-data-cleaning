import pandas as pd

def detect_outliers_iqr(series: pd.Series) -> pd.Series:
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1- 1.5 * IQR;
    upper_bound = Q3 + 1.5 * IQR
    return ((series < lower_bound) | (series > upper_bound))

# Example usage:
data = {
    "score": [10, 12, 13, 14, 15, 16, 17, 18, 100, 110]
}
df = pd.DataFrame(data)
outliers = detect_outliers_iqr(df["score"])
print(outliers)
