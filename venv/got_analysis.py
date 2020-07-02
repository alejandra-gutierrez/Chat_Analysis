import regex as re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime
from collections import Counter
import matplotlib
from matplotlib.font_manager import FontProperties
from plotly.subplots import make_subplots
import seaborn as sns
import os
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import random
import squarify  # pip install squarify (algorithm for treemap)
from nltk.corpus import stopwords


df = pd.read_csv('Data/all_episodes.csv')
df['line'] = df['line'].map(lambda x: x.lstrip('ser').rstrip('aAbBcC')) # Get rid of a set of characters
df['line'] = df['line'].str.replace('.', '')
df['line'] = df['line'].str.replace(',', '')

df.drop(df.columns[0], axis=1, inplace=True)
df["color"] = ""
df.loc[(df.sex == ' f'),'color']='red'
df.loc[(df.sex == ' m'),'color']='blue'

# print(tabulate(merged, tablefmt='psql'))

# ------------------------ per name tree map -----------------------------------
df2 = df.groupby(['name','sex', 'color'])['words'].sum().reset_index()

x1=pd.Series(df2['name'])
x2=pd.Series(df2['words'])
x3=pd.Series(df2['color'])
x2=x2.tolist()
x1=x1.tolist()
x3=x3.tolist()

# squarify.plot(sizes=x2, label=x1, color =x3,alpha=.7,bar_kwargs=dict(linewidth=1, edgecolor="#222222") )
# plt.axis('off')
# plt.show()
# ------------------------ per season stacked bar chart -----------------------------

df3 = df.groupby(['season','name','sex'])['words'].sum().reset_index(name='words_qt')
fig = px.bar(df3,
             x="season",
             y="words_qt",
             color='sex',
             barmode='stack')
# fig.show()

# ------------------------- per name wordcloud ---------------------------
df4 = df[df['name']  == "arya"]

words = ''
for i in df4.line.values:
    words += '{} '.format(i.lower()) # make all words lowercase

wd = pd.DataFrame(Counter(words.split()).most_common(200), columns=['word', 'frequency'])
wd = wd.iloc[50:]
print(wd)
data = dict(zip(wd['word'].tolist(), wd['frequency'].tolist()))
def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(30, 70)

wc = WordCloud(background_color='white',
               stopwords=STOPWORDS,
                width=800,
                height=400,
                max_words=200).generate_from_frequencies(data)
plt.figure(figsize=(10, 10))
plt.imshow(wc, interpolation='bilinear')
plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3),
           interpolation="bilinear")
plt.axis('off')
# plt.show()

# ------------------------ Exclamation marks ---------------------------

df['exc'] = df['line'].map(lambda x: x.count("!"))
df['ques'] = df['line'].map(lambda x: x.count("?"))

df5 = df.groupby(['name', 'sex'])['exc'].sum().reset_index()
df6 = df.groupby(['name'])['ques'].sum().reset_index()

expressions = df5.merge(df6, left_on='name', right_on='name')

fig = px.bar(expressions,
             x="name",
             y="exc",
             color='sex')
# fig.show()