#%%
import json, re, os, pandas as pd

## Functions
def sanitize_data(country):
    country = country.lower()
    country = re.sub(pattern='[^A-Za-z]', repl='-', string=country)
    country = re.sub('\-+', '-', country)
    if len(country) > 0:
        country = country[:-1] if country[-1] == '-' else country
    return country

def export(data, api):
    print(f'> Exporting: {api}')
    # Export to CSV
    try:
        # print('Exporting to CSV...')
        data.to_csv(f'api/{api}.csv', index=False)
        # print('Exported to CSV!')
    except Exception as e:
        print('[Error] - ', e)

    # Export to JSON
    try:
        # print('Exporting to JSON...')
        data = data.to_json(orient='records')
        f = open(f'api/{api}.json', 'w', encoding='utf-8')
        f.write(json.dumps(json.loads(data)))
        f.close()
    except Exception as e:
        print('[Error] - ', e)

### CASES
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
    df['date'] = df['date'].dt.strftime('%Y-%m-%d')
    df['country'] = df['country'].apply(sanitize_data)
    df['state'] = df['state'].apply(sanitize_data)

    export(data=df, api=f'cases/{t}')

    dfs[t] = df


joinCols = ['state', 'country', 'lat', 'long', 'date']

df = pd.merge(dfs['confirmed'], dfs['deaths'], how='left', on=joinCols)
df = pd.merge(df, dfs['recovered'], how='left', on=joinCols).fillna(0)

# Get latest date
today = df['date'].iloc[-1]

# Everything
export(data=df, api='cases/all')

# Global Level
df_global = df.groupby(['date']).agg({'confirmed':'sum', 'deaths':'sum', 'recovered':'sum'}).reset_index()
export(data=df_global, api='cases/global')

# Country Level
df_country = df.groupby(['date','country']).agg({'confirmed':'sum', 'deaths':'sum', 'recovered':'sum'}).reset_index()
export(data=df_country, api='cases/country')

### COUNTRIES
for country in df['country'].unique().tolist():

    # Export country data
    df_tmp_country = df[df['country'] == country]
    export(data=df_tmp_country, api=f'country/{country}')

    # Export state data
    if not os.path.isdir(f'api/country/{country}'):
        os.mkdir(f'api/country/{country}')

    for state in df_tmp_country['state'].unique().tolist():
        state = state if state else country
        df_tmp_state = df_tmp_country[df_tmp_country['state'] == state]
        export(data=df_tmp_state, api=f'country/{country}/{state}')

### DATE
for Date in df['date'].unique().tolist():
    df_date = df[df['date'] == Date]
    export(data=df_date, api=f'date/{Date}')

#%%
## STATS - WIP
stats = {}

# Now
stats['now'] = {}
stats['now']['global'] = df_global[df_global['date'] == today]
stats['now']['countries'] = df_country[df_country['date'] == today]

# N days ago
for Date in df['date'].unique().tolist():
    df_date = df[df['date'] == Date]
