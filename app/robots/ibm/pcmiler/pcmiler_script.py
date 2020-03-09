import pandas as pd


def run(filename: str) -> str:
    df: pd.DataFrame = pd.read_excel(filename)
    return df.head().to_string()
