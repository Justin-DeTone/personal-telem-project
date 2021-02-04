import pandas
import os
print(os.getcwd())

read_file = "data/heart_rate-2021-01-24.json"
read_file2 = "data/personal_telem.csv"
read_file3 = "data/distance-2021-01-14.json"

df = pandas.read_json(read_file)
df_survey = pandas.read_csv(read_file2)
df3 = pandas.read_json(read_file3)

print(df.info())
print(df3.info())

print(df_survey.info())

print(df_survey["Timestamp"].head(5))
df_survey["Timestamp"] = pandas.to_datetime(df_survey["Timestamp"].head(0), format = "%m/%d/%Y %H:%M:%S")
print(df_survey["Timestamp"].info())

#likely nan entries causing issues