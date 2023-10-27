
import pandas as pd
import numpy as np

def most_common_dtype(series):
    # Convert the types of each item in the series to strings and then count their occurrences
    type_counts = series.map(lambda x: str(type(x))).value_counts()
    
    # Get the most common type (as a string representation)
    common_type_str = type_counts.idxmax()
    
    return common_type_str


def filter_by_most_common_dtype(df, col_name):
    # Get the most common datatype of the column
    common_dtype_str = most_common_dtype(df[col_name])
    
    # Create a mask for rows where the data type is the most common
    mask = df[col_name].map(lambda x: str(type(x)) == common_dtype_str)
    
    # Use the mask to filter the DataFrame
    return df[mask]