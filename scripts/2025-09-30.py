import pandas as pd

#df 09:59-11:59pm
data = [
    ["30 September 2025 - 11:59 PM", 11.08, 124.06, 7, 3.8, "010 km N 67° E of City Of Bogo (Cebu)"],
    ["30 September 2025 - 11:49 PM", 11.18, 123.99, 30, 2.0, "015 km N 03° E of City Of Bogo (Cebu)"],
    ["30 September 2025 - 11:47 PM", 11.15, 124.16, 6, 2.6, "023 km N 60° E of City Of Bogo (Cebu)"],
    ["30 September 2025 - 11:42 PM", 11.12, 124.03, 31, 2.2, "010 km N 31° E of City Of Bogo (Cebu)"],
    ["30 September 2025 - 11:35 PM", 11.24, 123.92, 26, 3.4, "023 km N 17° W of City Of Bogo (Cebu)"],
    ["30 September 2025 - 11:33 PM", 11.04, 123.93, 8, 3.0, "005 km S 86° W of City Of Bogo (Cebu)"],
    ["30 September 2025 - 11:32 PM", 11.06, 124.06, 7, 2.2, "009 km N 77° E of City Of Bogo (Cebu)"],
    ["30 September 2025 - 11:25 PM", 11.13, 124.03, 7, 2.6, "011 km N 30° E of City Of Bogo (Cebu)"],
    ["30 September 2025 - 11:24 PM", 11.02, 123.96, 2, 2.8, "006 km S 10° W of City Of Bogo (Cebu)"],
    ["30 September 2025 - 11:12 PM", 11.05, 123.95, 80, 3.4, "004 km N 81° W of City Of Bogo (Cebu)"],
    ["30 September 2025 - 10:58 PM", 11.02, 123.90, 8, 2.9, "009 km S 69° W of City Of Bogo (Cebu)"],
    ["30 September 2025 - 10:52 PM", 11.00, 124.09, 5, 3.2, "013 km S 66° E of City Of Bogo (Cebu)"],
    ["30 September 2025 - 10:47 PM", 11.10, 123.87, 85, 2.4, "013 km N 62° W of City Of Bogo (Cebu)"],
    ["30 September 2025 - 10:32 PM", 11.03, 124.02, 5, 3.9, "005 km S 63° E of City Of Bogo (Cebu)"],
    ["30 September 2025 - 10:24 PM", 11.03, 124.02, 4, 4.0, "004 km S 68° E of City Of Bogo (Cebu)"],
    ["30 September 2025 - 09:59 PM", 11.10, 124.14, 5, 6.9, "019 km N 70° E of City Of Bogo (Cebu)"],
]

columns = ['Date - Time', 'Latitude', 'Longitude', 'Depth', 'Magnitude', 'Location']

df = pd.DataFrame(data, columns=columns)

df[['Date', 'Time']] = df['Date - Time'].str.split(' - ', expand=True)

# filter Bogo
df_bogo = df[df['Location'].str.contains("Bogo", case=False, na=False)]

# organize columns
df_bogo = df_bogo[['Date', 'Time', 'Magnitude', 'Depth', 'Location', 'Latitude', 'Longitude']]

# save CSV
df_bogo.to_csv("2025-09-30.csv", index=False)
print("Saved CSV successfully!")
