import pandas as pd
df = pd.read_csv('balance.txt',sep=' ')
# data = df
print (df)

#group the data by ethnicity and calculate the mean income for each group
average_income_base_ethnicity = df.groupby('Ethnicity')['Income'].mean()
print(average_income_base_ethnicity)

# compare the average balance for married and single individuals, 
# group the data by marital status and calculate the mean balance for each group. 
married  = df['Married'].apply(lambda x: 'yes' if x == 'yes' else '')
single   = df['Married'].apply(lambda x: 'no' if x == 'no' else '')
balance_and_marital_status_average = df.groupby('Married')['Balance'].mean()
print(balance_and_marital_status_average)

#To identify the highest and lowest income in the dataset
highest_income = df['Income'].max()
lowest_income = df['Income'].min()

print("Highest Income: ", highest_income)
print("Lowestest Income: ", lowest_income)

#number of cards recorded in our dataset
total_cards = df['Cards'].sum()
print("Total cards: ", total_cards)

#number of females and males in the dataset
f_count = df[df['Gender'] == 'Female'].count()['Gender']
m_count = df[df['Gender'] == 'Male'].count()['Gender']
print ("Number of female: ", f_count)
print ("Number of Male: ", m_count)