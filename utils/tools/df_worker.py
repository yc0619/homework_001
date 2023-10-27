
from utils.classes.df_helper import DataFrameHelper
from cfg import configs

class DataFrameCleaner(DataFrameHelper):

    def __init__(self, df):
        super().__init__()
        self.df = df
        self.common_types = []
    
    def filter_bad_apples(self, col_name):
        
        self.df = self.filter_by_most_common_dtype(col_name=col_name)
        self.common_types.append(self.common_type)


class DataFrameWorker(DataFrameCleaner):

    def __init__(self, df):
        super().__init__(df)
        self.feature = dict()
    
    def processing(self):
    
        for col_name in self.df:
            
            this_col = self.df[col_name]
            self.filter_bad_apples(col_name)
            if self.common_type not in configs.target_common_type:
                self.feature[col_name] = dict(max=max(this_col), min=min(this_col))
            else:
                self.feature[col_name] = list(set(this_col))
        
        return self.common_types, self.feature