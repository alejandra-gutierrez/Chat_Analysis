import regex as re
import pandas as pd
import matplotlib.pyplot as plt
import emoji
import numpy as np
from prettytable import PrettyTable
from tabulate import tabulate
import plotly.express as px
from plotly.subplots import make_subplots
from tabulate import tabulate
from datetime import datetime
from collections import Counter
import mplcairo
import matplotlib
from matplotlib.font_manager import FontProperties

df=pd.read_csv('conversation_Apolline.csv')

df = df.dropna(how = 'all')
df.drop(['3'], axis=1, inplace=True)
df.rename(columns={"0": "Date", "1": "name", "2":"message"}, inplace=True)
df = df.dropna() # Drop empty values

df['date'] = pd.to_datetime(df['Date'], format = '%d-%m-%y %H:%M:%S')
df['hour'] = df['date'].dt.hour
df['weekday'] = df['date'].dt.weekday
print(tabulate(df[50:100], headers='keys', tablefmt='psql'))
df = df.set_index(pd.DatetimeIndex(df['Date']))

# ------------ Plot message frequency over days -------------------

day_freq = df.resample('D').count()
day_freq.drop(day_freq.columns[0], axis = 1, inplace = True)
day_freq=day_freq.reset_index()

# Plot number 1 --------- Over whole period ----------------
fig = px.line(day_freq, x="Date", y="message")
# fig.show()

# Plot number 2 ------------ Hour or weekday ----------------
df1 = df.groupby(["hour"]).count().reset_index()
fig = px.bar(df1, y="message", x="hour", color='hour')
# fig.show()

# -------------------- Who sends more messages ------------------
df2 = df.groupby(["name"]).count().reset_index()

fig = px.bar(df2,
             y=df.groupby(["name"]).size(),
             x="name",
             color='name')
# fig.show()
# ------------------------------- Emojis ---------------------------
Alex = df[df['name']  == " Alex "]
Apolline = df[df['name']  == " Apolline "]


emojis_Alex=[]
for string in Alex['message']:
    my_str = str(string)
    for each in my_str:
        if each in emoji.UNICODE_EMOJI:
            emojis_Alex.append(each)

emojis_Apolline=[]
for string in Apolline['message']:
    my_str = str(string)
    for each in my_str:
        if each in emoji.UNICODE_EMOJI:
            emojis_Apolline.append(each)

freq_Alex = dict(Counter(i for sub in emojis_Alex for i in set(sub))) #This is a dictionary
sort_orders1 = sorted(freq_Alex.items(), key=lambda x: x[1], reverse=True)

freq_Apolline = dict(Counter(i for sub in emojis_Apolline for i in set(sub))) #This is a dictionary
sort_orders2 = sorted(freq_Apolline.items(), key=lambda x: x[1], reverse=True)

res_alex = sort_orders1[0:10]
res_apo = sort_orders2[0:10]

labels, ys = zip(*res_apo)
xs = np.arange(len(labels))
p1 = plt.bar(xs, ys, 0.8,color="lightblue")
# plt.show()



