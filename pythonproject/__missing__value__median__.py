"""
Berbeda dengan mean pada sesi sebelumnya,
median digunakan untuk data-data yang memiliki sifat outlier yang kuat.
 Kenapa median dipilih? Median merupakan nilai tengah yang artinya bukan
 hasil dari perhitungan yang melibatkan data outlier. Pada beberapa kasus,
 data outlier dianggap mengganggu dan sering dianggap noisy karena bisa
 mempengaruhi distribusi kelas dan mengganggu analisa pada klasterisasi (clustering).
"""

import pandas as pd

csv_data = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/shopping_data_missingvalue.csv")

print(csv_data.median())