import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


CREDENTIALS_ROUTE = 'credentials.json'  
SHEET_NAME = 'Disponibilidad de horario FC25 Trompetacos' 


scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_ROUTE, scope)
client = gspread.authorize(creds)

spreadsheet = client.open(SHEET_NAME)

worksheets = spreadsheet.worksheets()

dfs = []

for ws in worksheets:
    data = ws.get('A1:H25')
    if data and len(data) > 1:
        headers = data[0]
        clean_rows = [row for row in data[1:] if len(row) == len(headers)]
        if clean_rows:
            df = pd.DataFrame(clean_rows, columns=headers)
            df['worksheet_name'] = ws.title  
            dfs.append(df)

df_total = pd.concat(dfs, ignore_index=True)

DAYS = ['LUNES', 'MARTES', 'MIÉRCOLES', 'JUEVES', 'VIERNES', 'SÁBADO', 'DOMINGO']
SCHEDULE_COL = df_total.columns[0]  

df_binario = df_total[DAYS].applymap(lambda x: 1 if str(x).strip().upper() == 'X' else 0)
df_binario[SCHEDULE_COL] = df_total[SCHEDULE_COL]

df_heatmap = df_binario.groupby(SCHEDULE_COL).sum()

df_heatmap = df_heatmap.reindex(df_total[SCHEDULE_COL].unique())

plt.figure(figsize=(12, 8))
sns.heatmap(df_heatmap, annot=True, fmt='d', cmap='YlOrRd')
plt.title('Heatmap of the most popular time slots')
plt.ylabel('Time')
plt.xlabel('Day')
plt.tight_layout()
plt.savefig('heatmap.png', dpi=300)
plt.show()

df_best = df_heatmap >= 3

plt.figure(figsize=(12, 8))
sns.heatmap(df_best, annot=df_heatmap, fmt='d', cmap='Greens', cbar=False)
plt.title('best time to play')
plt.ylabel('Time')
plt.xlabel('Day')
plt.tight_layout()
plt.savefig('best_time_to_play.png', dpi=300)
plt.show() 