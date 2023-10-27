from abc import ABC, abstractclassmethod

import numpy as np
import pandas


class DataFrameHelper(ABC):

    def __init__(self):
        self.df = None
        self.common_type = None
    
    # outlier detector - dataframe - cleaner
    def most_common_dtype(self, this_col):
        
        # Convert the types of each item in the series to strings and then count their occurrences
        type_counts = this_col.map(lambda x: str(type(x))).value_counts()
        # Get the most common type (as a string representation)
        self.common_type = type_counts.idxmax()
        
        return self.common_type

    def filter_by_most_common_dtype(self, col_name):

        # Get the most common datatype of the column
        self.common_type = self.most_common_dtype(self.df[col_name])
        # Create a mask for rows where the data type is the most common
        mask = self.df[col_name].map(lambda x: str(type(x)) == self.common_type)
        
        # Use the mask to filter the DataFrame
        return self.df[mask]