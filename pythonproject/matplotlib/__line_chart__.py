import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv('https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/retail_raw_reduced.csv')
dataset.groupby(['order_month'])['gmv'].sum().plot()
plt.show()

#Mengubah foigure size
plt.figure(figsize=(15,5))
dataset.groupby(['order_month'])['gmv'].sum().plot()
plt.show()

#Menambahkan Tittle dan Axis Label