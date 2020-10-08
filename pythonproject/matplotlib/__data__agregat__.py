import pandas as pd
import datetime

dataset = pd.read_csv('https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/retail_raw_reduced.csv')
monthly_amount = dataset.groupby('order_month')['gmv'].sum().reset_index()
print(monthly_amount)