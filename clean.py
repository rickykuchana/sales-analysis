import json                                    # read and write JSON files
import pandas as pd                            # the data tool; "pd" is the standard nickname

with open("recalls_raw.json") as f:            # open the raw data file for reading
    all_recalls = json.load(f)                 # parse the JSON text into a Python list of dicts

df = pd.DataFrame(all_recalls)                 # turn the list of dicts into a DataFrame (each dict = one row)
print(df.shape)                                # (rows, columns) - confirms 125 records loaded

df = df.drop_duplicates(subset="NHTSACampaignNumber")   # remove rows sharing a campaign number; keeps the first
print(df.shape)                                # confirms the drop: 125 -> 123

df["ReportReceivedDate"] = pd.to_datetime(     # convert the date column from string to real datetime
    df["ReportReceivedDate"],                  # the column to convert
    format="%d/%m/%Y"                          # NHTSA's pattern: day/month/4-digit-year
)
print(df["ReportReceivedDate"].dtype)          # should print datetime64[ns], not object

df["Make"] = df["Make"].str.strip().str.upper()
df["Model"] = df["Model"].str.strip().str.upper()

print(df["Make"].unique())

