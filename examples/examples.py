#%%
import requests, os, json
import pandas as pd, numpy as np, plotly.express as px
from urllib.request import urlopen

# Functions
'''
# Input:
api: Type of the API call
args: The value for the requested API call

# Output:
Pandas DataFrame
'''
covid_api = lambda api, args: pd.read_csv(f'https://raw.githubusercontent.com/Pragith/covid19-api/master/api/{api}/{args}.csv')

#%%
# Ex - Eric - 1
df = covid_api(api='date', args='2020-04-03')
df.tail()

# Ex - Eric - 2
df = covid_api(api='country', args='canada/ontario')
df.tail()
##

#%%
## Ex-1
# Get global cases by country
case = 'country'
df = covid_api(api='cases', args=case)
print(f'Case: {case}')
print(df.tail())
df.to_csv(f'ex-1-global-by-country.csv', index=False)

# Chart:
fig = px.line(df, x='date', y='confirmed', color='country', title=f'Daily cases for <b>all countries</b>:')
fig.show()
fig.write_image(f'ex-1-global-by-country.png')


#%%
## Ex-2
# Get country == 'canada'
country = 'canada'
df = covid_api(api='country', args=country)
print(f'Country: {country}')
print(df.tail())
df.to_csv(f'ex-2-{country}.csv', index=False)

# Chart:
fig = px.line(df, x='date', y='confirmed', color='country', title=f'Daily cases for <b>{country.capitalize()}</b>:')
fig.show()
fig.write_image(f'ex-2-{country}-daily-cases.png')

fig = px.bar(df, x='date', y='confirmed_new', color='country', title=f'Daily new cases for <b>{country.capitalize()}</b>:')
fig.show()
fig.write_image(f'ex-2-{country}-daily-new-cases.png')

#%%
## Ex-3 (WIP)
# Don't plot against time. Go crazy!
case = 'country'
df = covid_api(api='cases', args=case)
df.to_csv(f'ex-3.csv', index=False)

# Chart:
fig = px.line(df, x='confirmed', y='confirmed_new', color='country', title=f'Trajectory of COVID-19 Confirmed Cases for <b>all countries</b>:')
fig.show()
fig.write_image(f'ex-3.png')

#%%
## Ex-4
# Fetch metadata
covid_api(api='dimensions', args='country')
covid_api(api='dimensions', args='state')
covid_api(api='dimensions', args='countries_states')


#%%
## Ex-5
# Map (WIP)
# Get country == 'us'
country = 'canada'
df = covid_api(api='country', args=country)
df.tail()
#%%

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                   dtype={"fips": str})
fig = px.choropleth_mapbox(df, geojson=counties, locations='fips', color='unemp',
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           labels={'unemp':'unemployment rate'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()


#%%
# df4 = df3.copy()
# df4['confirmed_log'] = df4['confirmed'].apply(np.log)
# df4['confirmed_new_log'] = df4['confirmed_new'].apply(np.log)
# df4.tail()
