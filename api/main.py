#%%
import pandas as pd
import json

#%%
## Functions
def clean_country(country):
    country = country.lower()
    country = re.sub(pattern='[^A-Za-z]', repl='-', string=country)
    country = re.sub('\-+', '-', country)
    country = country[:-1] if country[-1] == '-' else country
    return country

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
    df['country'] = df['country'].apply(clean_country)

    df.to_csv(f'api/cases/{t}.csv', index=False)

    dfs[t] = df


joinCols = ['state', 'country', 'lat', 'long', 'date']

df = pd.merge(dfs['confirmed'], dfs['deaths'], how='left', on=joinCols)
df = pd.merge(df, dfs['recovered'], how='left', on=joinCols).fillna(0)

# Get latest date
today = df['date'].iloc[-1]

# Everything
df.to_csv(f'api/cases/all.csv', index=False)

# Global Level
df_global = df.groupby(['date']).agg({'confirmed':'sum', 'deaths':'sum', 'recovered':'sum'}).reset_index()
df_global.to_csv(f'api/cases/global.csv', index=False)

# Country Level
df_country = df.groupby(['date','country']).agg({'confirmed':'sum', 'deaths':'sum', 'recovered':'sum'}).reset_index()
df_country.to_csv(f'api/cases/country.csv', index=False)

# %%
### COUNTRIES
for country in df['country'].unique().tolist():
    df_tmp = df[df['country'] == country]
    df_tmp.to_csv(f'api/country/{country}.csv', index=False)


# %%
### DATE
for Date in df['date'].unique().tolist():
    df_date = df[df['date'] == Date]

    df_date.to_csv(f'api/date/{Date}.csv', index=False)


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
