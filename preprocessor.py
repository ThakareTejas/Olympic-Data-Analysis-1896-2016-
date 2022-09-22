import pandas as pd

def preprocess(df,region_df):

    # filtering for summmer olympics
    df=df[df['Season']=='Summer']
    #merge with region_df
    df=df.merge(region_df,on='NOC',how='left')
    #dropping duplicates
    df.drop_duplicates(inplace=True)
    #one_hot_encoding
    df= pd.concat([df, pd.get_dummies(df['Medal'])],axis=1)
    return df