import pandas as pd
import numpy as np
import json
import csv

def getParsedDF():
    df = pd.read_json('Stock List.json')
    df['date'] = pd.to_datetime(df['date'])
    return df

