import pandas
import os
print(os.getcwd())

read_file = "data/heart_rate-2021-01-24.json"
df = pandas.read_json(read_file)

print(df.head(5))

