#Install Pandas
pip install pandas

#Importing Pandas
import pandas as pd

# Pandas DataFrame
df = fruit = pd.DataFrame({'Apples':[35, 41],'Bananas':[21,34]}, index=['2017 Sales', '2018 Sales'])

#Display DataFrame
fruit #or use 'df'

#Saving DataFrame to CSV
df.to_csv('fruit.csv')