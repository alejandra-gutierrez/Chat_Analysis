import regex as re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
import plotly.express as px
from plotly.subplots import make_subplots
from tabulate import tabulate
from datetime import datetime
from collections import Counter
import matplotlib
from matplotlib.font_manager import FontProperties
from plotly.subplots import make_subplots
import seaborn as sns
from wordcloud import WordCloud


df = pd.read_csv(r'Data/season1/e9.txt',  sep=":",  error_bad_lines=False)
print(df.shape)
# print(tabulate(df, tablefmt='psql',headers='keys'))

if df.shape[1] ==2:
    df.reset_index(inplace=True)
    df.drop(df.columns[0], axis = 1, inplace = True)

df = df.dropna() # Drop empty values
df.columns = ["person", "line"]
# print(df.head(30))
# print(df.info())
# print(df.shape)

# read_file = pd.read_csv(r'got_characters.txt', header = None,  error_bad_lines=False)
# read_file.to_csv(r'characters.csv', index=None)

df1 = pd.read_csv('characters.csv')
df1.drop(df1.columns[0], axis = 1, inplace = True)
# --------------------------- Format dataframes for merging ------------------------------
df['person'] = df['person'].str.lower()
df['person'] = df['person'].str.replace('/',' ')
df['person']=df['person'].str.replace(r"\(.*\)","") # Delete everything between the brackets
df['person']=df['person'].str.replace(r'^(\s*(?:\S+\s+){1})\S+',r'\1') # Delete last name
df['person'] = df['person'].str.strip()  # Delete preceding spaces

df1['name']= df1['name'].str.lower()
df1['name']=df1['name'].str.replace(r'^(\s*(?:\S+\s+){1})\S+',r'\1') # Delete last name
df1['name'] = df1['name'].str.strip() # Delete preceding spaces
df1.loc[(df1.name == 'khal'),'name']='khal drogo'

# print(df1.name.unique())
# --------------------------------- Merge dataframes ----------------------
merged = df1.merge(df, left_on='name', right_on='person')
merged['words'] = [len(x.split()) for x in merged['line'].tolist()]

# print(tabulate(merged, tablefmt='psql'))
# print(tabulate(merged, tablefmt='psql'))
merged1 = merged.groupby(['sex'])['words'].sum().reset_index()


