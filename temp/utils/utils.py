

from pyspark.sql.functions import min as pyspark_min, max as pyspark_max


def ask_unique(df, col_name):
    
    col_list = df.select(col_name).distinct().collect()
    data_unique = sorted([row[col_name] for row in col_list])

    return sorted(data_unique)

def ask_range(df, col_name):

    min_val = df.agg(pyspark_min(col_name)).collect()[0][0]
    max_val = df.agg(pyspark_max(col_name)).collect()[0][0]

    return dict(min=min_val, max=max_val)


