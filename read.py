import pandas
import os
print(os.getcwd())

read_file = "data/heart_rate-2021-01-24.json"
read_file2 = "data/personal_telem.csv"
read_file3 = "data/distance-2021-01-14.json"

df_heart = pandas.read_json(read_file)
df_survey = pandas.read_csv(read_file2)
df3 = pandas.read_json(read_file3)



#drop some survey entries
df_survey.dropna(axis=0, how="any", subset=["Timestamp"], inplace=True)

#Convert to datetime
pandas.to_datetime(df_survey["Timestamp"].head(0))


df_survey.rename(columns={"Timestamp": "time", "Rate your current mood (1: negative, 5: positive)": "mood", "Rate your current energy level": "energy",
	"Do you feel as though you could currently work on a complex problem?": "complex_problem", "Are you any of the following?": "tags",
	"Rate Lower Back Soreness (5 severe)": "back_soreness", "Add any notes/timestamps": "notes", 
	"Rate your current mental speed (0: slow, 3: can focus well; 5: mind is jittery/moving quickly)": "mental_speed"}, inplace=True)

df_survey.dropna(axis=0, how="any", subset=["mood", "energy", "complex_problem"], inplace=True)

print(df_survey.info())
print(df_survey.head(10))


break_out = lambda x: pandas.Series([x[key] for key in x])

add = df_heart["value"].apply(break_out)
add.rename(columns={0: "bpm", 1: "confidence"}, inplace=True)

df_heart_2 = pandas.concat([df_heart["dateTime"], add], axis=1)

print(df_heart_2.info())
print(df_heart_2.head(10))