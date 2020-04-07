import numpy as np
import csv
import pandas as pd

df = pd.read_csv('datafile.csv', index_col = "Id")
print(df.index)
df.info()

while(True):
	inp = input("Enter Your Sno.")
	if str(inp).lower() == "stop":
		break

	else:
		numb = int(inp)
		mark = df.iat[numb, df.columns.get_loc('Marks')]
		print(mark)
		l1 = len(df[df.Marks > mark])
		l2 = len(df[df.Marks == mark])
		print("Rank is", l1 + 1, " tied between ", l2)