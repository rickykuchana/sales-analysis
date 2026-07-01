import pandas as pd 
from sqlalchemy import create_engine 

df = pd.read_csv("sales.csv")
engine = create_engine("postgresql+psycopg2://rickykuchana@localhost:5432/training") 
df.to_sql("sales", engine, if_exists="replace", index=False)
print("Data loaded successfully!")
print(df.head())