import pandas as pd
import numpy as np

# Load the diabetes dataset
df = pd.read_csv('diabetes.csv')
class Remove_outliers():
    def __init__(self):
        self.cols=list(df.columns)
    def log_transformation(self,df):
        for col in self.cols:
            col_index = self.cols.index(col)
            print(f'col: {col} index: {col_index}')
            floor_value = df[col].quantile(.25)
            cap_value = df[col].quantile(.75)
            new_col_name = f'{col}_log'

            # Define a function to apply log transformation
            def log_transform(x):
                if x > cap_value or x < floor_value:
                    if x > 0:
                        return np.log(x)
                    else:
                        return x  # Keep zero or negative values unchanged
                else:
                    return x

            df[new_col_name] = df.iloc[:, col_index].map(log_transform)
        return df
    def medium_transformation(self,df):
        for col in self.cols:
            col_index=self.cols.index(col)
            median=df[col].quantile(.50)
            exream=df[col].quantile(.95)
            new_col_name=f'{col}_median'
            df[new_col_name]=np.where(df.iloc[:,col_index]>exream,median,df.iloc[:,col_index])
        return df


out=Remove_outliers()
df_log=out.log_transformation(df)
print(f'log transformaion')
print(df_log[['Glucose','Glucose_log']].head())
df_median=out.medium_transformation(df)
print('median transformaiton')
print(df_median[['Glucose','Glucose_median']])
