import pandas as pd
import datetime

dataset = pd.read_csv('https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/retail_raw_reduced.csv')
print('Ukuran dataset: %d baris dan %d kolom\n' % dataset.shape)
print('Lima data teratas:')
print(dataset.head())

#Menggunakan datetime untuk pengubahan waktu
dataset['order_month'] = dataset['order_date'].apply(lambda x:
                         datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
print(dataset.head())

#Penambahan kolom GMV pada dataset
dataset['gmv'] = dataset['item_price']*dataset['quantity']
print('Ukuran dataset: %d baris dan %d kolom\n' % dataset.shape)
print('Lima data teratas:')
print(dataset.head())

"""dataset['new_column'] = dataset['item_price'].apply(lambda x: x*2)
print(dataset.head())"""



