#%%
import pandas as pd
import json

# Build a single dataframe from 3 types of datasets
dfs = {}

def cases(request):    
    for t in ['confirmed', 'deaths', 'recovered']:
    
        # Get one type of dataset
        df = pd.read_csv(f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_{t}_global.csv')

        df = df.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long']).fillna('')

        df.rename(columns={
            'Province/State':'state',
            'Country/Region': 'country',
            'Lat': 'lat',
            'Long': 'long',
            'variable': 'date',
            'value': t
        }, inplace=True)

        df['date_epoch'] = pd.to_datetime(df['date'])
        df['date'] = df['date_epoch'].dt.strftime('%Y-%m-%d')
    
        dfs[t] = df.to_json(orient='records')

    return json.dumps(dfs), 200, {'Content-Type': 'application/json'}
