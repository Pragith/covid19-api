#%%
import json, re, os, pandas as pd
from shutil import rmtree

## Functions
unique_vals = lambda l: l.unique().tolist()

def sanitize_data(data):
    data = re.sub('\-+', '-', string=re.sub(pattern='[^A-Za-z]', repl='-', string=data.lower()))
    if len(data) > 0:
        data = data[:-1] if data[-1] == '-' else data
    return data

def export(data, api):
    print(f'> Exporting: {api}')

    # Export to CSV
    try:
        data.to_csv(f'api/{api}.csv', index=False)        
    except Exception as e:
        print('[Error] - ', e)

    # Export to JSON
    try:
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

    df_grouped = df.groupby(['country', 'state', 'lat', 'long'])
    new_dfs = []
    for k,grouped_df in df_grouped:
        grouped_df = grouped_df.reset_index()      
        grouped_df.loc[:,f'{t}_new'] = grouped_df[t] - grouped_df[t].shift(1, fill_value=0)        
        new_dfs.append(grouped_df)
    df = pd.concat(new_dfs)

    export(data=df, api=f'cases/{t}')

    dfs[t] = df

joinCols = ['state', 'country', 'lat', 'long', 'date']
groupByCols = {'confirmed':'sum', 'deaths':'sum', 'recovered':'sum', 'confirmed_new':'sum', 'deaths_new':'sum', 'recovered_new':'sum'}

df = pd.merge(dfs['confirmed'], dfs['deaths'], how='left', on=joinCols)
df = pd.merge(df, dfs['recovered'], how='left', on=joinCols).fillna(0)

# Get latest date
today = df['date'].iloc[-1]

# Everything
export(data=df, api='cases/all')

# Global Level
df_global = df.groupby(['date']).agg(groupByCols).reset_index()
export(data=df_global, api='cases/global')

# Country Level
df_country = df.groupby(['date','country']).agg(groupByCols).reset_index()
export(data=df_country, api='cases/country')

#%%

df[df['country'] == 'canada'].groupby(['country', 'date']).agg(groupByCols).reset_index()
#%%
### COUNTRIES
for country in unique_vals(df['country']):

    # Export country data
    df_tmp_country = df[df['country'] == country]    
    df_tmp_country_main = df[df['country'] == country].groupby(['date', 'country', 'state', 'lat', 'long']).agg(groupByCols).reset_index()
    #df_tmp_country_main['lat'] = df_tmp_country['lat'].iloc[0]
    #df_tmp_country_main['long'] = df_tmp_country['long'].iloc[0]

    export(data=df_tmp_country_main, api=f'country/{country}')

    # Export state data
    if os.path.isdir(f'api/country/{country}'):
        rmtree(f'api/country/{country}')
    os.mkdir(f'api/country/{country}')

    for state in unique_vals(df_tmp_country['state']):
        state = state if state else country
        df_tmp_state = df_tmp_country[df_tmp_country['state'] == state]
        export(data=df_tmp_state, api=f'country/{country}/{state}')

#%%
### DATE
for Date in unique_vals(df['date']):
    df_date = df[df['date'] == Date]
    export(data=df_date, api=f'date/{Date}')


### DIMENSIONS
countries_states = df[df['date'] == today][['country', 'state', 'lat', 'long']]

for dim in ['country', 'state', 'date']:
    df_dim = pd.DataFrame({ dim: unique_vals(df[dim]) })
    export(data=df_dim, api=f'dimensions/{dim}')

export(data=countries_states, api=f'dimensions/countries_states')
#%%
# ## STATS - WIP
# TODO - Create datasets for everything based on charts required
# stats = {}

# # Now
# stats['now'] = {}
# stats['now']['global'] = df_global[df_global['date'] == today]
# stats['now']['countries'] = df_country[df_country['date'] == today]

# # N days ago
# for Date in df['date'].unique().tolist():
#     df_date = df[df['date'] == Date]
