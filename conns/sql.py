from google.colab import drive
drive.mount('/content/drive')

# connect to database in google drive
conn = sqlite3(connect(gdrivePath+'caers.db'))

# connect to a database in google drive
conn = sqlite3.connect(gdrivePath+"caers.db") 

def execSQL(conn,query):
  conn.execute(query) # execute an SQL query
  conn.commit() # "commit" that query in order to make its action permanent