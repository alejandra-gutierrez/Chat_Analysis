import regex as re
import pandas as pd
import matplotlib.pyplot as plt
import emoji

# print(emoji.demojize("☕"))
# print("\U0001f63b:")
# print("\u2615:")

file = open('Apolline.txt',encoding="utf8")
data = file.read()
file.close()

data = data.replace(']', '],')
data = data.replace('\U0001f63b:', ',')
data = data.replace("\u2615", ",")
data = data.replace("\u200e", "")
data = data.replace(': ', '')
data = data.replace(',,,', '')
data = data.replace('[', '')
data = data.replace(']', '')
data = data.replace('\n',',\n')
data = data.replace('audio',',')
data = data.replace('omitted','')

print(type(data))
print(data[850:1050])

text_file = open("test.txt", "w")
n = text_file.write(data)

read_file = pd.read_csv(r'test.txt', header = None,  error_bad_lines=False)
# read_file.to_csv (r'conversation_Apolline.csv', index=None)


