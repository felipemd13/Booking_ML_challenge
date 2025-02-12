#%%
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

# df_train = pd.read_csv('datasets/train_set.csv')
def preprocess(df):
    df['checkin'] = pd.to_datetime(df['checkin'])
    df['checkout'] = pd.to_datetime(df['checkout'])
    df['duration'] = (df['checkout'] - df['checkin']).dt.days
    return df

# df_train = preprocess(df_train)

def plot_graph(x_series, y_series, title, x_label, y_label, legend, limit_x=None, type='line'):
    plt.figure(figsize=(10, 5))
    if not isinstance(x_series[0], list):
        x_series = [x_series]
        y_series = [y_series]
    for i in range(len(x_series)):
        if type == 'bar':
            plt.bar(x_series[i], y_series[i])
        elif type == 'scatter':
            plt.scatter(x_series[i], y_series[i])
        elif type == 'line':
            plt.plot(x_series[i], y_series[i])
        elif type == 'log':
            plt.loglog(x_series[i], y_series[i])
        elif type == 'barlog':
            plt.bar(x_series[i], y_series[i])
            plt.yscale('log')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend(legend)
    if limit_x:
        plt.xlim(limit_x)
    plt.show()
# plot utrip_id
# df_train['city_id'].value_counts().plot(kind='hist', bins=100)

# # plot #reservation in cities and countries vs fq items
# y_values = df_train['city_id'].value_counts().values
# x_values = [i for i in range(len(y_values))]
# y_values_country = df_train['hotel_country'].value_counts().values
# x_values_country = [i for i in range(len(y_values_country))]
# plt.figure(figsize=(10, 5))
# plt.loglog(x_values, y_values)
# plt.loglog(x_values_country, y_values_country)
# plt.xlabel('#of reservations')
# plt.ylabel('frequency')
# plt.legend(['city_id', 'hotel_country'])
# plt.show()

# df_train_travel = df_train.groupby('utrip_id').agg({
#     'city_id': pd.Series.nunique,
#     'hotel_country': pd.Series.nunique,
#     'duration': 'sum',
#     'checkin': 'first',
#     'checkout': 'last'
# })
# df_train_travel['total_days_grouped'] = df_train_travel['duration'].apply(lambda x: 30 if x > 30 else x)

# print(df_train_travel.head())

# y_values = df_train_travel['total_days_grouped'].value_counts().values
# x_values = df_train_travel['total_days_grouped'].value_counts().index
# plt.figure(figsize=(10, 5))
# plt.bar(x_values, y_values)
# plt.xlabel('total days')
# plt.ylabel('frequency')
# plt.show()

# %%
