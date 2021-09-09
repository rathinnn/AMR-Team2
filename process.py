import pandas as pd
import numpy as np
import json
import csv
from parse import getParsedDF

def getCurDF(df,symbol,start_date,end_date):
    dfSym = df.loc[df['symbol'] == symbol]
    mask = (dfSym['date'] >= start_date) & (dfSym['date'] <= end_date)
    df2 = dfSym.loc[mask,['date','symbol','close','high','low','open']]

    return df2



