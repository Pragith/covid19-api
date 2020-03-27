#%%
import pandas as pd

## Variables


## Functions


## Execution

# Build a single dataframe from 3 types of datasets
dfs = {}
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

    df['date'] = pd.to_datetime(df['date'])

    dfs[t] = df

# %%
dfs['confirmed'].to_json(orient='records')
# %%
dfs['confirmed']['date'].dt.strftime('%Y-%m-%d')

# %%
