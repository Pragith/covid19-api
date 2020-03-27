#%%
import pandas as pd
import requests, json

def country(request):    
    c = request.args.get('country')
    casesURL = 'https://us-central1-prag-gcp-2019.cloudfunctions.net/cases'

    # Get one type of dataset
    df = pd.read_csv(f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_{t}_global.csv')

    df['date_epoch'] = pd.to_datetime(df['date'])
    df['date'] = df['date'].dt.strftime('%Y-%m-%d')

    return df.to_json(orient='records')



#%%
## Sandbox
c = 'India'
casesURL = 'https://us-central1-prag-gcp-2019.cloudfunctions.net/cases'

# Download all the cases
cases = json.loads(requests.get(casesURL).text)



# %%
for t in ['confirmed', 'deaths', 'recovered']:
    df = cases[t]

    # Filter by country
    df = df[df['country'] == c]

    