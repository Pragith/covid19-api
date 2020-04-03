

```python
import requests, os, json
import cufflinks as cf, pandas as pd, numpy as np, plotly.express as px, chart_studio.plotly as py

# Functions
covid_api = lambda api, args: pd.read_csv(f'https://raw.githubusercontent.com/Pragith/covid19-api/master/api/{api}/{args}.csv')
```


```python
## Ex-1
# Get global cases by country
case = 'country'
df = covid_api(api='cases', args=case)
print(f'Case: {case}')
display(df.tail())
df.to_csv(f'ex-1-global-by-country.csv', index=False)

# Chart:
fig = px.line(df, x='date', y='confirmed', color='country', title=f'Daily cases for <b>all countries</b>:')
fig.write_image(f'ex-1-global-by-country.png')
py.iplot(fig, filename='ex-1-global-by-country') #fig.show()
#fig = df.iplot(asFigure=True, yTitle='Confirmed Cases', xTitle='Date', title='Daily cases for <b>all countries</b>:', x='date', y='confirmed', color='country')

```

    Case: country
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>country</th>
      <th>confirmed</th>
      <th>deaths</th>
      <th>recovered</th>
      <th>confirmed_new</th>
      <th>deaths_new</th>
      <th>recovered_new</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>13027</th>
      <td>2020-04-02</td>
      <td>venezuela</td>
      <td>146</td>
      <td>5</td>
      <td>43.0</td>
      <td>3</td>
      <td>2</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>13028</th>
      <td>2020-04-02</td>
      <td>vietnam</td>
      <td>233</td>
      <td>0</td>
      <td>75.0</td>
      <td>15</td>
      <td>0</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>13029</th>
      <td>2020-04-02</td>
      <td>west-bank-and-gaza</td>
      <td>161</td>
      <td>1</td>
      <td>18.0</td>
      <td>27</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>13030</th>
      <td>2020-04-02</td>
      <td>zambia</td>
      <td>39</td>
      <td>1</td>
      <td>0.0</td>
      <td>3</td>
      <td>1</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>13031</th>
      <td>2020-04-02</td>
      <td>zimbabwe</td>
      <td>9</td>
      <td>1</td>
      <td>0.0</td>
      <td>1</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>






        <iframe
            width="100%"
            height="525px"
            src="https://plotly.com/~Pragith/1.embed"
            frameborder="0"
            allowfullscreen
        ></iframe>
        




```python
## Ex-2
# Get country == 'canada'
country = 'canada'
df = covid_api(api='country', args=country)
print(f'Country: {country}')
display(df.tail())
df.to_csv(f'ex-2-{country}.csv', index=False)

# Chart:
fig = px.line(df, x='date', y='confirmed', color='country', title=f'Daily cases for <b>{country.capitalize()}</b>:')
fig.write_image(f'ex-2-{country}-daily-cases.png')
py.iplot(fig, filename=f'ex-2-{country}-daily-cases') #fig.show()

```

    Country: canada
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>country</th>
      <th>state</th>
      <th>confirmed</th>
      <th>deaths</th>
      <th>recovered</th>
      <th>confirmed_new</th>
      <th>deaths_new</th>
      <th>recovered_new</th>
      <th>lat</th>
      <th>long</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1075</th>
      <td>2020-04-02</td>
      <td>canada</td>
      <td>prince-edward-island</td>
      <td>22</td>
      <td>0</td>
      <td>0.0</td>
      <td>1</td>
      <td>0</td>
      <td>0.0</td>
      <td>53.9333</td>
      <td>-116.5765</td>
    </tr>
    <tr>
      <th>1076</th>
      <td>2020-04-02</td>
      <td>canada</td>
      <td>quebec</td>
      <td>5518</td>
      <td>36</td>
      <td>0.0</td>
      <td>907</td>
      <td>3</td>
      <td>0.0</td>
      <td>53.9333</td>
      <td>-116.5765</td>
    </tr>
    <tr>
      <th>1077</th>
      <td>2020-04-02</td>
      <td>canada</td>
      <td>recovered</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>53.9333</td>
      <td>-116.5765</td>
    </tr>
    <tr>
      <th>1078</th>
      <td>2020-04-02</td>
      <td>canada</td>
      <td>saskatchewan</td>
      <td>206</td>
      <td>3</td>
      <td>0.0</td>
      <td>13</td>
      <td>0</td>
      <td>0.0</td>
      <td>53.9333</td>
      <td>-116.5765</td>
    </tr>
    <tr>
      <th>1079</th>
      <td>2020-04-02</td>
      <td>canada</td>
      <td>yukon</td>
      <td>6</td>
      <td>0</td>
      <td>0.0</td>
      <td>1</td>
      <td>0</td>
      <td>0.0</td>
      <td>53.9333</td>
      <td>-116.5765</td>
    </tr>
  </tbody>
</table>
</div>






        <iframe
            width="100%"
            height="525px"
            src="https://plotly.com/~Pragith/7.embed"
            frameborder="0"
            allowfullscreen
        ></iframe>
        




```python
fig = px.bar(df, x='date', y='confirmed_new', color='country', title=f'Daily new cases for <b>{country.capitalize()}</b>:')
fig.write_image(f'ex-2-{country}-daily-new-cases.png')
py.iplot(fig, filename=f'ex-2-{country}-daily-new-cases') #fig.show()
```





        <iframe
            width="100%"
            height="525px"
            src="https://plotly.com/~Pragith/9.embed"
            frameborder="0"
            allowfullscreen
        ></iframe>
        




```python
## Ex-3 (WIP)
# Don't plot against time. Go crazy!
case = 'country'
df = covid_api(api='cases', args=case)
df.to_csv(f'ex-3.csv', index=False)

# Chart:
fig = px.line(df, x='confirmed', y='confirmed_new', color='country', title=f'Trajectory of COVID-19 Confirmed Cases for <b>all countries</b>:')
fig.write_image(f'ex-3.png')
py.iplot(fig, filename=f'ex-3.png') #fig.show()

```





        <iframe
            width="100%"
            height="525px"
            src="https://plotly.com/~Pragith/11.embed"
            frameborder="0"
            allowfullscreen
        ></iframe>
        




```python
## Ex-4
# Fetch metadata
covid_api(api='dimensions', args='country')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>afghanistan</td>
    </tr>
    <tr>
      <th>1</th>
      <td>albania</td>
    </tr>
    <tr>
      <th>2</th>
      <td>algeria</td>
    </tr>
    <tr>
      <th>3</th>
      <td>andorra</td>
    </tr>
    <tr>
      <th>4</th>
      <td>angola</td>
    </tr>
    <tr>
      <th>5</th>
      <td>antigua-and-barbuda</td>
    </tr>
    <tr>
      <th>6</th>
      <td>argentina</td>
    </tr>
    <tr>
      <th>7</th>
      <td>armenia</td>
    </tr>
    <tr>
      <th>8</th>
      <td>australia</td>
    </tr>
    <tr>
      <th>9</th>
      <td>austria</td>
    </tr>
    <tr>
      <th>10</th>
      <td>azerbaijan</td>
    </tr>
    <tr>
      <th>11</th>
      <td>bahamas</td>
    </tr>
    <tr>
      <th>12</th>
      <td>bahrain</td>
    </tr>
    <tr>
      <th>13</th>
      <td>bangladesh</td>
    </tr>
    <tr>
      <th>14</th>
      <td>barbados</td>
    </tr>
    <tr>
      <th>15</th>
      <td>belarus</td>
    </tr>
    <tr>
      <th>16</th>
      <td>belgium</td>
    </tr>
    <tr>
      <th>17</th>
      <td>belize</td>
    </tr>
    <tr>
      <th>18</th>
      <td>benin</td>
    </tr>
    <tr>
      <th>19</th>
      <td>bhutan</td>
    </tr>
    <tr>
      <th>20</th>
      <td>bolivia</td>
    </tr>
    <tr>
      <th>21</th>
      <td>bosnia-and-herzegovina</td>
    </tr>
    <tr>
      <th>22</th>
      <td>botswana</td>
    </tr>
    <tr>
      <th>23</th>
      <td>brazil</td>
    </tr>
    <tr>
      <th>24</th>
      <td>brunei</td>
    </tr>
    <tr>
      <th>25</th>
      <td>bulgaria</td>
    </tr>
    <tr>
      <th>26</th>
      <td>burkina-faso</td>
    </tr>
    <tr>
      <th>27</th>
      <td>burma</td>
    </tr>
    <tr>
      <th>28</th>
      <td>burundi</td>
    </tr>
    <tr>
      <th>29</th>
      <td>cabo-verde</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>151</th>
      <td>slovenia</td>
    </tr>
    <tr>
      <th>152</th>
      <td>somalia</td>
    </tr>
    <tr>
      <th>153</th>
      <td>south-africa</td>
    </tr>
    <tr>
      <th>154</th>
      <td>spain</td>
    </tr>
    <tr>
      <th>155</th>
      <td>sri-lanka</td>
    </tr>
    <tr>
      <th>156</th>
      <td>sudan</td>
    </tr>
    <tr>
      <th>157</th>
      <td>suriname</td>
    </tr>
    <tr>
      <th>158</th>
      <td>sweden</td>
    </tr>
    <tr>
      <th>159</th>
      <td>switzerland</td>
    </tr>
    <tr>
      <th>160</th>
      <td>syria</td>
    </tr>
    <tr>
      <th>161</th>
      <td>taiwan</td>
    </tr>
    <tr>
      <th>162</th>
      <td>tanzania</td>
    </tr>
    <tr>
      <th>163</th>
      <td>thailand</td>
    </tr>
    <tr>
      <th>164</th>
      <td>timor-leste</td>
    </tr>
    <tr>
      <th>165</th>
      <td>togo</td>
    </tr>
    <tr>
      <th>166</th>
      <td>trinidad-and-tobago</td>
    </tr>
    <tr>
      <th>167</th>
      <td>tunisia</td>
    </tr>
    <tr>
      <th>168</th>
      <td>turkey</td>
    </tr>
    <tr>
      <th>169</th>
      <td>uganda</td>
    </tr>
    <tr>
      <th>170</th>
      <td>ukraine</td>
    </tr>
    <tr>
      <th>171</th>
      <td>united-arab-emirates</td>
    </tr>
    <tr>
      <th>172</th>
      <td>united-kingdom</td>
    </tr>
    <tr>
      <th>173</th>
      <td>uruguay</td>
    </tr>
    <tr>
      <th>174</th>
      <td>us</td>
    </tr>
    <tr>
      <th>175</th>
      <td>uzbekistan</td>
    </tr>
    <tr>
      <th>176</th>
      <td>venezuela</td>
    </tr>
    <tr>
      <th>177</th>
      <td>vietnam</td>
    </tr>
    <tr>
      <th>178</th>
      <td>west-bank-and-gaza</td>
    </tr>
    <tr>
      <th>179</th>
      <td>zambia</td>
    </tr>
    <tr>
      <th>180</th>
      <td>zimbabwe</td>
    </tr>
  </tbody>
</table>
<p>181 rows × 1 columns</p>
</div>




```python
covid_api(api='dimensions', args='state')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>state</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>australian-capital-territory</td>
    </tr>
    <tr>
      <th>2</th>
      <td>new-south-wales</td>
    </tr>
    <tr>
      <th>3</th>
      <td>northern-territory</td>
    </tr>
    <tr>
      <th>4</th>
      <td>queensland</td>
    </tr>
    <tr>
      <th>5</th>
      <td>south-australia</td>
    </tr>
    <tr>
      <th>6</th>
      <td>tasmania</td>
    </tr>
    <tr>
      <th>7</th>
      <td>victoria</td>
    </tr>
    <tr>
      <th>8</th>
      <td>western-australia</td>
    </tr>
    <tr>
      <th>9</th>
      <td>alberta</td>
    </tr>
    <tr>
      <th>10</th>
      <td>british-columbia</td>
    </tr>
    <tr>
      <th>11</th>
      <td>grand-princess</td>
    </tr>
    <tr>
      <th>12</th>
      <td>manitoba</td>
    </tr>
    <tr>
      <th>13</th>
      <td>new-brunswick</td>
    </tr>
    <tr>
      <th>14</th>
      <td>newfoundland-and-labrador</td>
    </tr>
    <tr>
      <th>15</th>
      <td>nova-scotia</td>
    </tr>
    <tr>
      <th>16</th>
      <td>ontario</td>
    </tr>
    <tr>
      <th>17</th>
      <td>prince-edward-island</td>
    </tr>
    <tr>
      <th>18</th>
      <td>quebec</td>
    </tr>
    <tr>
      <th>19</th>
      <td>saskatchewan</td>
    </tr>
    <tr>
      <th>20</th>
      <td>diamond-princess</td>
    </tr>
    <tr>
      <th>21</th>
      <td>recovered</td>
    </tr>
    <tr>
      <th>22</th>
      <td>northwest-territories</td>
    </tr>
    <tr>
      <th>23</th>
      <td>yukon</td>
    </tr>
    <tr>
      <th>24</th>
      <td>anhui</td>
    </tr>
    <tr>
      <th>25</th>
      <td>beijing</td>
    </tr>
    <tr>
      <th>26</th>
      <td>chongqing</td>
    </tr>
    <tr>
      <th>27</th>
      <td>fujian</td>
    </tr>
    <tr>
      <th>28</th>
      <td>gansu</td>
    </tr>
    <tr>
      <th>29</th>
      <td>guangdong</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>51</th>
      <td>sichuan</td>
    </tr>
    <tr>
      <th>52</th>
      <td>tianjin</td>
    </tr>
    <tr>
      <th>53</th>
      <td>tibet</td>
    </tr>
    <tr>
      <th>54</th>
      <td>xinjiang</td>
    </tr>
    <tr>
      <th>55</th>
      <td>yunnan</td>
    </tr>
    <tr>
      <th>56</th>
      <td>zhejiang</td>
    </tr>
    <tr>
      <th>57</th>
      <td>faroe-islands</td>
    </tr>
    <tr>
      <th>58</th>
      <td>greenland</td>
    </tr>
    <tr>
      <th>59</th>
      <td>french-guiana</td>
    </tr>
    <tr>
      <th>60</th>
      <td>french-polynesia</td>
    </tr>
    <tr>
      <th>61</th>
      <td>guadeloupe</td>
    </tr>
    <tr>
      <th>62</th>
      <td>mayotte</td>
    </tr>
    <tr>
      <th>63</th>
      <td>new-caledonia</td>
    </tr>
    <tr>
      <th>64</th>
      <td>reunion</td>
    </tr>
    <tr>
      <th>65</th>
      <td>saint-barthelemy</td>
    </tr>
    <tr>
      <th>66</th>
      <td>st-martin</td>
    </tr>
    <tr>
      <th>67</th>
      <td>martinique</td>
    </tr>
    <tr>
      <th>68</th>
      <td>aruba</td>
    </tr>
    <tr>
      <th>69</th>
      <td>curacao</td>
    </tr>
    <tr>
      <th>70</th>
      <td>sint-maarten</td>
    </tr>
    <tr>
      <th>71</th>
      <td>bonaire-sint-eustatius-and-saba</td>
    </tr>
    <tr>
      <th>72</th>
      <td>bermuda</td>
    </tr>
    <tr>
      <th>73</th>
      <td>cayman-islands</td>
    </tr>
    <tr>
      <th>74</th>
      <td>channel-islands</td>
    </tr>
    <tr>
      <th>75</th>
      <td>gibraltar</td>
    </tr>
    <tr>
      <th>76</th>
      <td>isle-of-man</td>
    </tr>
    <tr>
      <th>77</th>
      <td>montserrat</td>
    </tr>
    <tr>
      <th>78</th>
      <td>anguilla</td>
    </tr>
    <tr>
      <th>79</th>
      <td>british-virgin-islands</td>
    </tr>
    <tr>
      <th>80</th>
      <td>turks-and-caicos-islands</td>
    </tr>
  </tbody>
</table>
<p>81 rows × 1 columns</p>
</div>




```python
covid_api(api='dimensions', args='countries_states')


```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>state</th>
      <th>lat</th>
      <th>long</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>afghanistan</td>
      <td>NaN</td>
      <td>33.000000</td>
      <td>65.000000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>albania</td>
      <td>NaN</td>
      <td>41.153300</td>
      <td>20.168300</td>
    </tr>
    <tr>
      <th>2</th>
      <td>algeria</td>
      <td>NaN</td>
      <td>28.033900</td>
      <td>1.659600</td>
    </tr>
    <tr>
      <th>3</th>
      <td>andorra</td>
      <td>NaN</td>
      <td>42.506300</td>
      <td>1.521800</td>
    </tr>
    <tr>
      <th>4</th>
      <td>angola</td>
      <td>NaN</td>
      <td>-11.202700</td>
      <td>17.873900</td>
    </tr>
    <tr>
      <th>5</th>
      <td>antigua-and-barbuda</td>
      <td>NaN</td>
      <td>17.060800</td>
      <td>-61.796400</td>
    </tr>
    <tr>
      <th>6</th>
      <td>argentina</td>
      <td>NaN</td>
      <td>-38.416100</td>
      <td>-63.616700</td>
    </tr>
    <tr>
      <th>7</th>
      <td>armenia</td>
      <td>NaN</td>
      <td>40.069100</td>
      <td>45.038200</td>
    </tr>
    <tr>
      <th>8</th>
      <td>australia</td>
      <td>australian-capital-territory</td>
      <td>-35.473500</td>
      <td>149.012400</td>
    </tr>
    <tr>
      <th>9</th>
      <td>australia</td>
      <td>new-south-wales</td>
      <td>-33.868800</td>
      <td>151.209300</td>
    </tr>
    <tr>
      <th>10</th>
      <td>australia</td>
      <td>northern-territory</td>
      <td>-12.463400</td>
      <td>130.845600</td>
    </tr>
    <tr>
      <th>11</th>
      <td>australia</td>
      <td>queensland</td>
      <td>-28.016700</td>
      <td>153.400000</td>
    </tr>
    <tr>
      <th>12</th>
      <td>australia</td>
      <td>south-australia</td>
      <td>-34.928500</td>
      <td>138.600700</td>
    </tr>
    <tr>
      <th>13</th>
      <td>australia</td>
      <td>tasmania</td>
      <td>-41.454500</td>
      <td>145.970700</td>
    </tr>
    <tr>
      <th>14</th>
      <td>australia</td>
      <td>victoria</td>
      <td>-37.813600</td>
      <td>144.963100</td>
    </tr>
    <tr>
      <th>15</th>
      <td>australia</td>
      <td>western-australia</td>
      <td>-31.950500</td>
      <td>115.860500</td>
    </tr>
    <tr>
      <th>16</th>
      <td>austria</td>
      <td>NaN</td>
      <td>47.516200</td>
      <td>14.550100</td>
    </tr>
    <tr>
      <th>17</th>
      <td>azerbaijan</td>
      <td>NaN</td>
      <td>40.143100</td>
      <td>47.576900</td>
    </tr>
    <tr>
      <th>18</th>
      <td>bahamas</td>
      <td>NaN</td>
      <td>25.034300</td>
      <td>-77.396300</td>
    </tr>
    <tr>
      <th>19</th>
      <td>bahrain</td>
      <td>NaN</td>
      <td>26.027500</td>
      <td>50.550000</td>
    </tr>
    <tr>
      <th>20</th>
      <td>bangladesh</td>
      <td>NaN</td>
      <td>23.685000</td>
      <td>90.356300</td>
    </tr>
    <tr>
      <th>21</th>
      <td>barbados</td>
      <td>NaN</td>
      <td>13.193900</td>
      <td>-59.543200</td>
    </tr>
    <tr>
      <th>22</th>
      <td>belarus</td>
      <td>NaN</td>
      <td>53.709800</td>
      <td>27.953400</td>
    </tr>
    <tr>
      <th>23</th>
      <td>belgium</td>
      <td>NaN</td>
      <td>50.833300</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>24</th>
      <td>belize</td>
      <td>NaN</td>
      <td>13.193900</td>
      <td>-59.543200</td>
    </tr>
    <tr>
      <th>25</th>
      <td>benin</td>
      <td>NaN</td>
      <td>9.307700</td>
      <td>2.315800</td>
    </tr>
    <tr>
      <th>26</th>
      <td>bhutan</td>
      <td>NaN</td>
      <td>27.514200</td>
      <td>90.433600</td>
    </tr>
    <tr>
      <th>27</th>
      <td>bolivia</td>
      <td>NaN</td>
      <td>-16.290200</td>
      <td>-63.588700</td>
    </tr>
    <tr>
      <th>28</th>
      <td>bosnia-and-herzegovina</td>
      <td>NaN</td>
      <td>43.915900</td>
      <td>17.679100</td>
    </tr>
    <tr>
      <th>29</th>
      <td>botswana</td>
      <td>NaN</td>
      <td>-22.328500</td>
      <td>24.684900</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>228</th>
      <td>syria</td>
      <td>NaN</td>
      <td>34.802075</td>
      <td>38.996815</td>
    </tr>
    <tr>
      <th>229</th>
      <td>taiwan</td>
      <td>NaN</td>
      <td>23.700000</td>
      <td>121.000000</td>
    </tr>
    <tr>
      <th>230</th>
      <td>tanzania</td>
      <td>NaN</td>
      <td>-6.369000</td>
      <td>34.888800</td>
    </tr>
    <tr>
      <th>231</th>
      <td>thailand</td>
      <td>NaN</td>
      <td>15.000000</td>
      <td>101.000000</td>
    </tr>
    <tr>
      <th>232</th>
      <td>timor-leste</td>
      <td>NaN</td>
      <td>-8.874217</td>
      <td>125.727539</td>
    </tr>
    <tr>
      <th>233</th>
      <td>togo</td>
      <td>NaN</td>
      <td>8.619500</td>
      <td>0.824800</td>
    </tr>
    <tr>
      <th>234</th>
      <td>trinidad-and-tobago</td>
      <td>NaN</td>
      <td>10.691800</td>
      <td>-61.222500</td>
    </tr>
    <tr>
      <th>235</th>
      <td>tunisia</td>
      <td>NaN</td>
      <td>34.000000</td>
      <td>9.000000</td>
    </tr>
    <tr>
      <th>236</th>
      <td>turkey</td>
      <td>NaN</td>
      <td>38.963700</td>
      <td>35.243300</td>
    </tr>
    <tr>
      <th>237</th>
      <td>uganda</td>
      <td>NaN</td>
      <td>1.000000</td>
      <td>32.000000</td>
    </tr>
    <tr>
      <th>238</th>
      <td>ukraine</td>
      <td>NaN</td>
      <td>48.379400</td>
      <td>31.165600</td>
    </tr>
    <tr>
      <th>239</th>
      <td>united-arab-emirates</td>
      <td>NaN</td>
      <td>24.000000</td>
      <td>54.000000</td>
    </tr>
    <tr>
      <th>240</th>
      <td>united-kingdom</td>
      <td>bermuda</td>
      <td>32.307800</td>
      <td>-64.750500</td>
    </tr>
    <tr>
      <th>241</th>
      <td>united-kingdom</td>
      <td>cayman-islands</td>
      <td>19.313300</td>
      <td>-81.254600</td>
    </tr>
    <tr>
      <th>242</th>
      <td>united-kingdom</td>
      <td>channel-islands</td>
      <td>49.372300</td>
      <td>-2.364400</td>
    </tr>
    <tr>
      <th>243</th>
      <td>united-kingdom</td>
      <td>gibraltar</td>
      <td>36.140800</td>
      <td>-5.353600</td>
    </tr>
    <tr>
      <th>244</th>
      <td>united-kingdom</td>
      <td>isle-of-man</td>
      <td>54.236100</td>
      <td>-4.548100</td>
    </tr>
    <tr>
      <th>245</th>
      <td>united-kingdom</td>
      <td>montserrat</td>
      <td>16.742500</td>
      <td>-62.187400</td>
    </tr>
    <tr>
      <th>246</th>
      <td>united-kingdom</td>
      <td>NaN</td>
      <td>55.378100</td>
      <td>-3.436000</td>
    </tr>
    <tr>
      <th>247</th>
      <td>united-kingdom</td>
      <td>anguilla</td>
      <td>18.220600</td>
      <td>-63.068600</td>
    </tr>
    <tr>
      <th>248</th>
      <td>united-kingdom</td>
      <td>british-virgin-islands</td>
      <td>18.420700</td>
      <td>-64.640000</td>
    </tr>
    <tr>
      <th>249</th>
      <td>united-kingdom</td>
      <td>turks-and-caicos-islands</td>
      <td>21.694000</td>
      <td>-71.797900</td>
    </tr>
    <tr>
      <th>250</th>
      <td>uruguay</td>
      <td>NaN</td>
      <td>-32.522800</td>
      <td>-55.765800</td>
    </tr>
    <tr>
      <th>251</th>
      <td>us</td>
      <td>NaN</td>
      <td>37.090200</td>
      <td>-95.712900</td>
    </tr>
    <tr>
      <th>252</th>
      <td>uzbekistan</td>
      <td>NaN</td>
      <td>41.377500</td>
      <td>64.585300</td>
    </tr>
    <tr>
      <th>253</th>
      <td>venezuela</td>
      <td>NaN</td>
      <td>6.423800</td>
      <td>-66.589700</td>
    </tr>
    <tr>
      <th>254</th>
      <td>vietnam</td>
      <td>NaN</td>
      <td>16.000000</td>
      <td>108.000000</td>
    </tr>
    <tr>
      <th>255</th>
      <td>west-bank-and-gaza</td>
      <td>NaN</td>
      <td>31.952200</td>
      <td>35.233200</td>
    </tr>
    <tr>
      <th>256</th>
      <td>zambia</td>
      <td>NaN</td>
      <td>-15.416700</td>
      <td>28.283300</td>
    </tr>
    <tr>
      <th>257</th>
      <td>zimbabwe</td>
      <td>NaN</td>
      <td>-20.000000</td>
      <td>30.000000</td>
    </tr>
  </tbody>
</table>
<p>258 rows × 4 columns</p>
</div>




```python

```
