import mysql.connector
import pandas as pd
data=pd.read_csv("onlinefoods_2.csv")


# preprocessiong the data
df=data.head(50).dropna()
df=df[['Age','Gender','Marital Status','Occupation']]   # selected only required columns from the dataframe.

# Database connection

mydb=mysql.connector.connect(host='localhost',user='root',password='Subbu@777')

mycursor=mydb.cursor()

# mycursor.execute('create database file_to_database')          # created a database
mycursor.execute('use file_to_database')
#mycursor.execute('create table onlinefoods_data(age text,Gender text,Marital_Status text,Occupation text)')      # created a table
colums_data=df.columns

# for _,row in df.iterrows():
#     sql = f"INSERT INTO onlinefoods_data (Age, Gender, Marital_Status, Occupation) VALUES (%s, %s, %s, %s)"
#     mycursor.execute(sql, tuple(row))
# mydb.commit()

# select records from the table
mycursor.execute('select * from onlinefoods_data')
for i in mycursor:
    print(i)


# select records with Age > 22

mycursor.execute('select * from onlinefoods_data where Age>22')
for i in mycursor:
    print(i)

mycursor.close()
