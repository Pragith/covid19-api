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
for t in ['confirmed', 'deaths']:

    # Get one type of dataset
    df = pd.read_csv(f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_{t}_US.csv')
    
    if 'Population' in df.columns:
        del df['Population']

    df = df.melt(id_vars=['UID','iso2','iso3','code3','FIPS','Admin2','Province_State','Country_Region','Lat','Long_','Combined_Key']).fillna('')

    df.rename(columns={
        'Province_State':'state',
        'Country_Region': 'country',
        'Admin2':'region',
        'Lat': 'lat',
        'Long_': 'long',
        'variable': 'date',
        'value': t
    }, inplace=True)

    df['date'] = pd.to_datetime(df['date'])
    df['date'] = df['date'].dt.strftime('%Y-%m-%d')
    df['country'] = df['country'].apply(sanitize_data)
    df['state'] = df['state'].apply(sanitize_data)
    df['region'] = df['region'].apply(sanitize_data)
    df[t] = df[t].astype('int64')

    df_grouped = df.groupby(['country', 'state', 'lat', 'long', 'UID','iso2','iso3','code3','FIPS','region','Combined_Key'])
    new_dfs = []
    for k,grouped_df in df_grouped:
        grouped_df = grouped_df.reset_index()      
        grouped_df.loc[:,f'{t}_new'] = grouped_df[t] - grouped_df[t].shift(1, fill_value=0)        
        new_dfs.append(grouped_df)
    df = pd.concat(new_dfs)
    if 'index' in df.columns:
        del df['index']

    dfs[t] = df

joinCols = ['date','country', 'state', 'lat', 'long', 'UID','iso2','iso3','code3','FIPS','region','Combined_Key']
groupByCols = {'confirmed':'sum', 'deaths':'sum', 'confirmed_new':'sum', 'deaths_new':'sum'}

df = pd.merge(dfs['confirmed'], dfs['deaths'], how='left', on=joinCols).fillna(0)
df = df[['date','country', 'state', 'lat', 'long', 'UID','iso2','iso3','code3','FIPS','region','Combined_Key', 'confirmed', 'confirmed_new', 'deaths', 'deaths_new']]

# Get latest date
today = df['date'].iloc[-1]

# Country Level
df_country = df.groupby(['date','country']).agg(groupByCols).reset_index()
export(data=df_country, api='cases/country')

### COUNTRIES
for country in unique_vals(df['country']):

    # Export country data
    df_tmp_country = df[df['country'] == country]    
    df_tmp_country_main = df[df['country'] == country].groupby(['date', 'country', 'state', 'lat', 'long', 'UID','iso2','iso3','code3','FIPS','region','Combined_Key']).agg(groupByCols).reset_index()

    export(data=df_tmp_country_main, api=f'country/{country}')

    # Export state data
    if os.path.isdir(f'api/country/{country}'):
        rmtree(f'api/country/{country}')
    os.mkdir(f'api/country/{country}')

    for state in unique_vals(df_tmp_country['state']):
        state = state if state else country
        df_tmp_state = df_tmp_country[df_tmp_country['state'] == state]
        export(data=df_tmp_state, api=f'country/{country}/{state}')

        # Export region data
        if os.path.isdir(f'api/country/{country}/{state}'):
            rmtree(f'api/country/{country}/{state}')
        os.mkdir(f'api/country/{country}/{state}')

        for region in unique_vals(df_tmp_state['region']):
            region = region if region else state
            df_tmp_region = df_tmp_state[df_tmp_state['region'] == region]
            export(data=df_tmp_region, api=f'country/{country}/{state}/{region}')


### DATE
for Date in unique_vals(df['date']):
    df_date = df[df['date'] == Date]
    export(data=df_date, api=f'date/{Date}_us')


# ### DIMENSIONS
# countries_states = df[df['date'] == today][['country', 'state', 'lat', 'long']]

# for dim in ['country', 'state', 'date']:
#     df_dim = pd.DataFrame({ dim: unique_vals(df[dim]) })
#     export(data=df_dim, api=f'dimensions/{dim}')

# export(data=countries_states, api=f'dimensions/countries_states')
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
