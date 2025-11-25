import pandas as pd
import requests
import io

url = "https://earthquake.phivolcs.dost.gov.ph/EQLatest-Monthly/2025/2025_October.html"

try:

    response = requests.get(url, verify=False)
    response.raise_for_status() 

  
    tables = pd.read_html(io.StringIO(response.text))

    if len(tables) > 2:
        
        df = tables[2]

        if 'Location' in df.columns:
            df_bogo = df[df['Location'].astype(str).str.contains("Bogo", case=False, na=False)]
            df_bogo.to_csv("2025-October.csv", index=False)
            print("Saved October CSV for Bogo City!")
        else:
            print("Error: 'Location' column not found in the parsed table. Please inspect the table structure.")
    else:
        print("No enough tables found on the page to parse the expected data.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")