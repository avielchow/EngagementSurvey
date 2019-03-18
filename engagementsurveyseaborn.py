import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

path = "C:\\Users\\aviel\\Desktop\\Coding\\52-Weeks-of-Code\\Engagement Survey"
data = pd.read_csv(path + "\Survey2018.csv")
questions = list(data.columns.values)

'''Delete Columns from Original'''

data.drop(questions[3:18], 1, inplace=True)
data.drop(questions[150:], 1, inplace=True)

''' Delete rows for M and F'''
data = data.loc[data["Sex"] == "ALL"]

''' convert to percentages'''
''' column (3/2, 4/2, 5/2), (7/6 8/6, 9/6), (11/10, 12/10, 13/10)... etc'''

for x in range(33):
    for y in range(3,134,4):  
        
        '''
        Remove NaN from all cells 
        
        submissions = data.iloc[x,y]
        unfavorable = data.iloc[x,y+1]
        neutral = data.iloc[x,y+2]
        favorable = data.iloc[x,y+3]
        '''

        if math.isnan(data.iloc[x,y]) == True:
            data.iloc[x,y] = 0

        if math.isnan(data.iloc[x,y+1]) == True:
            data.iloc[x,y+1] = 0

        if math.isnan(data.iloc[x,y+2]) == True:
            data.iloc[x,y+2] = 0

        if math.isnan(data.iloc[x,y+3]) == True:
            data.iloc[x,y+3] = 0


        data.iloc[x,y+1] = int((data.iloc[x,y+1]/float(data.iloc[x,y]))*100)
        data.iloc[x,y+2] = int((data.iloc[x,y+2]/float(data.iloc[x,y]))*100)
        data.iloc[x,y+3] = int((data.iloc[x,y+3]/float(data.iloc[x,y]))*100)
    
''' reset index'''
data = data.reset_index(drop = True)

'''Re-Defining Variables Based on new DataFrame'''
questions = list(data.columns.values)
branch = data.iloc[:,1]


''' Input - Which Question do you want statistics for? Enter a number'''

def user_input():
    user_input = ""
    while user_input != int:
        user_input = input("What Question do you want statistics on. Enter the number:")
        try:
            user_input = int(user_input)
            return user_input
            break
        except:
            pass


''' return correct chart
(y-2)/4 = x
4x + 2 = y

x - y
1 - 6
2 - 10
3 - 14
4 - 18
'''

chart = (user_input() * 4) + 2

plotdata = data.sort_values([questions[chart]]).reset_index(drop=True)

sns.set(style = "whitegrid")

f, ax = plt.subplots(figsize=(10,15))

for i, v in enumerate(plotdata[questions[chart]].iteritems()):     
    ax.text(v[1],i, "{:,}".format(v[1]), color='m', rotation=45)


sns.barplot(questions[chart],'Branch', data=plotdata)












data.to_csv(path + "\SurveyOutput.csv")
