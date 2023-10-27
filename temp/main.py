
from cfg import configs
from utils.utils import *

from pyspark.sql import SparkSession


"""
===============
= I-N-P-U-T-S =
===============

- Data type: str
    * acq_channel
    * app_channel

- Data type: bool
    * is_customer

- Data type: float
    * app_behavioral_score
    * requested_credit_limit
    * credit_bureau_score
    * stated_income

- classes: str
    * card_type
"""


if __name__ == "__main__":

    spk_session = SparkSession.builder.getOrCreate()
    df = spk_session.read.csv(str(configs.csv_data_path), header=True, inferSchema=True)
    df.show(truncate=False)


    """
    DATA TYPE: STRING / BOOL
    * ask unique
    """
    # init dict for preprocessing
    responce_dict = dict()
    for str_key in configs.str_cols:        
        responce_dict[str_key] = ask_unique(df=df, col_name=str_key)

    print(responce_dict)

    """
    DATA TYPE: FLOAT
    * ask range
    """

    for float_key in configs.float_cols:
        responce_dict[float_key] = ask_range(df, float_key)
    print(responce_dict)

