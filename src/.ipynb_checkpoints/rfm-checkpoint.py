import pandas as pd
from datetime import datetime

def create_rfm(df):

    # Reference date (last purchase + 1 day)
    snapshot_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)

    rfm = df.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
        'InvoiceNo': 'nunique',
        'Revenue': 'sum'
    })

    rfm.columns = ['Recency', 'Frequency', 'Monetary']

    return rfm.reset_index()
