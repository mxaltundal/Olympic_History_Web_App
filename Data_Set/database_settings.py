import pandas as pd
import sqlite3

# Load CSV data into a DataFrame
df = pd.read_csv(r'E:\BLG 317E\Project\Data_Set\Olympic_Athlete_Bio.csv')
df1 = pd.read_csv(r'E:\BLG 317E\Project\Data_Set\Olympic_Athlete_Event_Results.csv')
df2 = pd.read_csv(r'E:\BLG 317E\Project\Data_Set\Olympic_Games_Medal_Tally.csv')
df3 = pd.read_csv(r'E:\BLG 317E\Project\Data_Set\Olympic_Results.csv')
df4 = pd.read_csv(r'E:\BLG 317E\Project\Data_Set\Olympics_Country.csv')
df5 = pd.read_csv(r'E:\BLG 317E\Project\Data_Set\Olympics_Games.csv')

# Veritabanına bağlan
conn = sqlite3.connect("olympics.db")

# Insert data into MySQL table
df.to_sql('Olympic_Athlete_Bio', con=conn, if_exists='replace', index=False)
df1.to_sql('Olympic_Athlete_Event_Results', con=conn, if_exists='replace', index=False)
df2.to_sql('Olympic_Athlete_Medal_Tally', con=conn, if_exists='replace', index=False)
df3.to_sql('Olympic_Results', con=conn, if_exists='replace', index=False)
df4.to_sql('Olympic_Country', con=conn, if_exists='replace', index=False)
df5.to_sql('Olympic_Games', con=conn, if_exists='replace', index=False)

print("Data imported successfully.")
