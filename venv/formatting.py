import regex as re
import pandas as pd
import matplotlib.pyplot as plt
import emoji

# print(emoji.demojize("☕"))
# print("\U0001f63b:")
# print("\u2615:")

file = open('Data/SmileyKids.txt',encoding="utf8")
data = file.read()
file.close()

data = data.replace(']', '],')
# data = data.replace('\U0001f63b:', ',')
# data = data.replace("\u2615", ",")
data = data.replace("\u200e", "")
data = data.replace(',,,', '')
data = data.replace('[', '')
data = data.replace(']', '')
data = data.replace('\n',',\n')
data = data.replace('supervisión:','supervisión,')
# data = data.replace('SK Digital:','SK Digital,')
# data = data.replace('Jaras Paula:','Jaras Paula,')
# data = data.replace('Reponedores:','Reponedores,')
# data = data.replace('Accounting sK:','Accounting sK,')
# data = data.replace('Conductor SK:','Conductor SK,')
# data = data.replace('kids:','kids,')
# data = data.replace('Kids:','Kids,')
data = data.replace('2571‬:','2571,')
# data = data.replace('Ventas SK:','Ventas SK,')
# data = data.replace('Supervisor SK:','Supervisor SK,')
# data = data.replace('Caroline Vlerick:','Caroline Vlerick,')
data = data.replace('\u202a','')
data = data.replace('\xa0','')
data = data.replace('Jose  Conductor SK:','Person1,')
data = data.replace('Humberto  SK Supervisor Reponedores:','Person2,')
data = data.replace('Cristian  Miranda Supervisor SK:','Person3,')
data = data.replace('Collin  Smiley kids:','Person4,')
data = data.replace('Andrea Ruiztagle (Chile) Smiley Kids:','Person5,')
data = data.replace('Charlotte Haskell Smiley kids:','Person6,')
data = data.replace('Daniel Ventas SK:','Person7,')
data = data.replace('Elias Accounting sK:','Person8,')
data = data.replace('+56981452571','Person9')
data = data.replace('Jaras Paula:','Person10,')
data = data.replace('Cristian  SK Digital:','Person11,')
data = data.replace('Caroline Vlerick:','Boss,')



# data = data.replace('audio',',')
# data = data.replace('omitted','')
# data = data.replace('image','')


print(type(data))
print(data[1000:3000])

text_file = open("test.txt", "w")
n = text_file.write(data)

read_file = pd.read_csv(r'test.txt', header = None,  error_bad_lines=False)
read_file.to_csv(r'conversation_SK.csv', index=None)

#
