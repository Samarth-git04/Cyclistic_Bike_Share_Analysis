import pandas as pd
import os

months = ["202407", "202408", "202409", "202410", "202411", "202412",
          "202501", "202502", "202503", "202504", "202505", "202506"]

script_dir = os.path.dirname(os.path.abspath(__file__))

dfs = []
for month in months:
    filename = f"{script_dir}\\{month}-divvy-tripdata.csv"
    df = pd.read_csv(filename)
    dfs.append(df)
    print(f"Loaded {filename}")

if dfs:
    combined_df = pd.concat(dfs, ignore_index=True)
    combined_df.to_csv("All_data.csv", index=False)
    print("Combined CSV saved as All_data.csv")
else:
    print("No files were loaded. No combined CSV created.")