import sqlite3
import pandas
con=sqlite3.connect("edgar_idx.db")
cur=con.cursor()
sql="SELECT cik, COUNT(type) from idx GROUP BY cik"
sql2 = "SELECT cik,type, COUNT(type) from idx GROUP BY cik, type"
table = pandas.read_sql_query(sql,con)
table2 = pandas.read_sql_query(sql2,con)

table.to_csv('CIKFormCount.csv')
table2.to_csv('CIKFormCountbytype.csv')
