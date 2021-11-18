import os
import glob
import pandas as pd


path = r'C:\Users\dhan004\Desktop\file path'                    
all_files = glob.glob(os.path.join(path, "*.csv")) 
names = [os.path.basename(x) for x in glob.glob(path+'\*.csv')] 

list_ = []
for file_ in all_files:
    list_.append(pd.read_csv(file_,sep=',', parse_dates=[0], infer_datetime_format=True,header=None ))  

df = pd.DataFrame()
for file_ in all_files:
    file_df = pd.read_csv(file_,sep=',', parse_dates=[0], infer_datetime_format=True,header=None )
    file_df['file_name'] = file_
    df = df.append(file_df)
    df.to_csv('test4.csv')