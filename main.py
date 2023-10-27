
from cfg import configs

import pandas as pd
from utils.tools.df_worker import DataFrameWorker


if __name__ == "__main__":

    # load csv
    df = pd.read_csv(configs.csv_data_path)

    df_worker = DataFrameWorker(df=df)
    _, feature_dict = df_worker.processing()
    cleaned_df = df_worker.df
    print(cleaned_df)
    print(feature_dict)


    # get range

    # data preprocessing

    # dataloader

    # utils.train
    # model
    # train/ val: cross validation
    # tensorboard
    
    # val test monitor
    # save test - val < 7%
