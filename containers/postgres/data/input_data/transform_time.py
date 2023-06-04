import pandas as pd
from datetime import timedelta
import numpy as np

df=pd.read_csv('../../../../data/OnlineRetail.csv')

df['InvoiceDate']=pd.to_datetime(df.InvoiceDate)

df['CustomerID']= df['CustomerID'].fillna('').astype(str).str.replace(".0","",regex=False)

df["InvoiceDate"] = df["InvoiceDate"] + timedelta(days=365*12)

df.to_csv('OnlineRetail.csv',index=False)