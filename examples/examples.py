#%%
import requests, os, json
import pandas as pd, numpy as np, plotly.express as px

# Functions
covid_api = lambda api, args: pd.read_csv(f'https://raw.githubusercontent.com/Pragith/covid19-api/master/api/{api}/{args}.csv')


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
# df4 = df3.copy()
# df4['confirmed_log'] = df4['confirmed'].apply(np.log)
# df4['confirmed_new_log'] = df4['confirmed_new'].apply(np.log)
# df4.tail()
