def make_series(dates):
    import pandas as pd
    index = pd.DatetimeIndex(dates)
    series = pd.Series(index=index)
    return series

def add_months_since_start_col(start_date, df):
    import numpy as np
    df['months_since_start'] = ((df.index - start_date)/np.timedelta64(1, 'M'))
    df['months_since_start'] = df.months_since_start.round()
    return df


# used for foursquare api
def time_elapsed_since(epochtime):
    import datetime
    ts = datetime.datetime.fromtimestamp(epochtime).strftime('%Y-%m-%d %H:%M:%S')
    return ts


# Yelp API
def business_search():
    import requests
    headers = {"Authorization": "Bearer V-w71bBGGOyWbXNZuBEwIQkhzVmZIe9AExAO_Wh4yXkV3JhZijUT5fFyjAec5oOXUVBBUl8V3e6SbhiQZM9yBKTmFEPdJXQnXbF705rRPc4e3EV4ORH1RquZcTWvWnYx"}
    endpoint = "https://api.yelp.com/v3/businesses/search?location=houston&categories=bars&rating=3.5&sort_by=review_count"
    return requests.get(endpoint, headers=headers).json()['businesses']



# TX Mixed Drink Receipts API, Max Wine Bar

# tx-revenues-pd.ipynb
# df = pd.read_csv('revenue_data.csv', index_col = 0)
# response = requests.get("https://data.texas.gov/resource/naix-2893.json?location_name=MAX%27S%20WINE%20DIVE")
def retrieve_receipt_dates_and_rev(restaurant_values):
    receipts = []
    for value in max_wine_bar_values:
        date = value['obligation_end_date_yyyymmdd']
        revenue = value['total_receipts']
        receipts.append({'date': date, 'revenue': revenue, 'address': value['location_address']})
    return receipts

def gather_receipts_for(address):
    receipts = retrieve_receipt_dates_and_rev(values)
    return list(filter(lambda receipt: receipt['address'] == address,restaurants_receipts))


### Simple Linear Regression
def plot_scatter():
    import matplotlib.pyplot as plt
    X = np.array(df[column]).reshape(-1, 1)
    return plt.scatter(X, Y,  color='black')

def simple_linear_regression(x_list, y_list):
    import numpy as np
    import statsmodels.api as sm
    X = np.array(x_list).reshape(-1, 1)
    X2 = sm.add_constant(X)
    model = sm.OLS(y_list, X2)
    fitted_model = model.fit()
    print(fitted_model.summary())
    
def sklearn_linear_regression(X, Y):
    from sklearn import linear_model
    regr = linear_model.LinearRegression()
    #     Ylist = np.array(Y)
    Xlist = np.array(X).reshape(-1, 1)
    model = regr.fit(Xlist, Y)
    return {'coef': regr.coef_, 'intercept': regr.intercept_, 'regr': regr}

def plot_model(regr, x_values, y_values):
    #     x_values can either be new or the original X values
    import matplotlib.pyplot as plt
    y_pred = regr.predict(x_values)
    plt.scatter(x_values, y_values,  color='black')
    return plt.plot(x_values, y_pred, color='blue', linewidth=3)

# Read Json
def read_json(file):
    import json
    with open(file, 'r') as filehandle:  
        reviews = json.load(filehandle)
    return reviews