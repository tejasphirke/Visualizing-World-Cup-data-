# Visualizing World Cup Data With Seaborn
'''
Visualizing World Cup Data With Seaborn
For this project you will be exploring data from the Fifa World Cup from 1930-2014 to analyze trends and discover insights about the world’s game, fútbol!

This Fifa World Cup data is from Kaggle. Kaggle is a platform for data science competitions that hosts many datasets online.

Using Seaborn you will create a series of plots that explore aggregates and distribution across the goals scored in World Cup games.

A little primer on the Fifa World Cup:
The FIFA World Cup, or simply the World Cup, is an international fútbol competition where 32 countries qualify to send teams made up of the best players from that nation to compete against each other for the World Cup championship.

The World Cup championship has been awarded every four years since the inaugural tournament in 1930, except in 1942 and 1946 when it was not held because of the Second World War.

The current format of the tournament involves 32 teams competing for the title at venues within the host nation over a period of one month.
'''
import codecademylib3_seaborn
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('WorldCupMatches.csv')
df_goals = pd.read_csv('goals.csv')

df['Total Goals'] = df['Home Team Goals'] + df['Away Team Goals']

sns.set_style('whitegrid')
sns.set_context('notebook', font_scale = 1.25)
f, ax = plt.subplots(figsize=(12,7))
ax = sns.barplot(x=df['Year'], y = df['Total Goals'])

ax.set_title('Average Number Of Goals Scored In World Cup Matches By Year')
plt.show()

f, ax2 = plt.subplots(figsize=(12,7))
ax2 = sns.boxplot(x='year', y='goals', 
                  data = df_goals, 
				  palette='Spectral')
ax2.set_title('Goals Visualization')

plt.show()