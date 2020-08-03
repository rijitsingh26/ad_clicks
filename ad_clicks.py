# importing the Pandas Library:
import pandas as pd

# setting the PyCharm IDE console display size (NOTE: not necessary for terminal users):
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 2000)

# importing the data of the csv file:
df = pd.read_csv('views.csv')
print(df.head(10), "\n")

# counting the number of users for each utm_source:
views = pd.DataFrame(df.groupby('utm_source') \
                     .user_id.count() \
                     .reset_index())
print(views, "\n")

# displaying the users who clicked on the ad:
df['is_click'] = ~df.ad_click_timestamp.isnull()
print(df.head(), "\n")

# creating a new Dataframe for each utm_source with number of users who clicked/who didn't:
clicks_by_source = df.groupby(['utm_source', 'is_click']) \
    .user_id.count() \
    .reset_index()
print(clicks_by_source, "\n")

# pivoting the Dataframe to have separate columns for the users who clicked/who didn't:
clicks_pivot = clicks_by_source.pivot(
    index='utm_source',
    columns='is_click',
    values='user_id'
).reset_index()
print(clicks_pivot, "\n")

# creating a new column calculating the percentage of users who clicked:
clicks_pivot['percent_clicked'] = clicks_pivot[True] * 100 / (clicks_pivot[True] + clicks_pivot[False])
print(clicks_pivot, "\n")

# creating a new Dataframe displaying the number of users who watched which ad:
ad_type = df.groupby('experimental_group') \
    .user_id.count() \
    .reset_index()
print(ad_type, "\n")

# creating a new Dataframe comparing the number of users to whom the ads were shown:
greater_percentage = df.groupby(['experimental_group', 'is_click']) \
    .user_id.count() \
    .reset_index() \
    .pivot(
    index='experimental_group',
    columns='is_click',
    values='user_id'
).reset_index()
print(greater_percentage, "\n")

# creating separate Dataframes for ads A and B:
a_clicks = df[df.experimental_group == 'A']
b_clicks = df[df.experimental_group == 'B']
print(a_clicks.head(), "\n\n", b_clicks.head(), "\n")

# creating new Dataframes for A and B sorted by days:
a_by_day = a_clicks.groupby('day') \
    .user_id.count() \
    .reset_index()
b_by_day = b_clicks.groupby('day') \
    .user_id.count() \
    .reset_index()
print("A:\n", a_by_day, "\n\n", "B:\n", b_by_day, "\n")

# Pivoting the Dataframes to have the separate columns for users who clicked/who didn't:
a_clicks_pivot = a_clicks.groupby(['is_click', 'day']) \
    .user_id.count() \
    .reset_index() \
    .pivot(
    index='day',
    columns='is_click',
    values='user_id'
).reset_index()

b_clicks_pivot = b_clicks.groupby(['is_click', 'day']) \
    .user_id.count() \
    .reset_index() \
    .pivot(
    index='day',
    columns='is_click',
    values='user_id'
).reset_index()

# creating new columns in each of the Dataframe calculating the percentage of users who clicked(by day)"
a_clicks_pivot['percent_clicked'] = a_clicks_pivot[True] * 100 / (a_clicks_pivot[True] + a_clicks_pivot[False])
b_clicks_pivot['percent_clicked'] = b_clicks_pivot[True] * 100 / (b_clicks_pivot[True] + b_clicks_pivot[False])
print(a_clicks_pivot, "\n\n", b_clicks_pivot)