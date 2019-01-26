#!/usr/bin/env python3



import psycopg2  # Imports the psycopg2 library.


# A method to connect to the news database.

def connect():
    		
	try:
		conn = psycopg2.connect("dbname=news")
		return conn
	except Exception as err:
		print(err)		
	

# A method that accepts the result of an sql query,
# and two headers.


def display(ans, header1, header2):
    num2 = 0
    # A for loop to write text to the output file NewsResults.txt
    for num2 in range(len(ans)):
        a = ans[num2]  # A variable to store a string to be written
    # to the output file.
        b = str(a[1])
        # Writes a formated string to the outpu file.
        file.write("%-5s - %-35s %-7s - %-7s\r\n"
                   % (header1, a[0], b, header2))

    file.write('\n')  # Writes a blank line to the output file.
    file.close()  # Closes the output file.

# A method to open the output file NewsResults.txt for appending.


def fileOpen():
    try:
        newsFile = open('NewsResults.txt', 'a')
        return newsFile
    except Exception as err:
        print(err)

# A method to search the database. This method accepts a
# cursor object which is connected to the database, a
# query to search the database, and two headers to write
# to the output file.


def searchData(curr, sql1, header1, header2):
    curr.execute(sql1)
    res = curr.fetchall()
    display(res, header1, header2)


header1 = 'Title'  # A string variable to hold the title header.
header2 = 'Views'  # A string variable to hold the views header.
header3 = 'Author'  # A string variable to hold the author header.
header4 = 'Date'  # A string variable to hold the date header.

# A string variable to hold the precentage header.
header5 = 'Percentage of Errors'

# An sql query that selects title of each article in the database,
# and then counts the total number of of times this article is accesed
# in the log table. It# then joins the log table and extracts the path
# and compares this to the slug column in the articles tables.

sql1 = 'select a.title, count(*) as count from log join \
articles a on substring(path,10)=slug group by title \
order by count desc limit 3'

# An sql query the selects the name of the author from the log database.
# It then counts the total number of times an article written by each author
# is viewed.

sql2 = 'select au.name, count(*) from log join articles\
 a on substring(path,10)=slug join authors au on au.id \
 = a.author group by name order by count desc'

# Sql query's that selects the date from the log database. It then
# uses a case statement to count the numbeer of times a query recieved a 404
# error, and divides this by the total number of queries for each day.
# The query then multiplies the reult by 100 to show the percentage of errors
# for each day and rounds the reuslt to two decimal places.

sql3 = 'select date(time) as date ,round(((SUM(CASE WHEN log.status=\
\'404 NOT FOUND\' THEN 1 ELSE 0 END))/((count(date(time))*1.0))\
*100),2)as a from log group by date having round(((SUM(CASE WHEN \
log.status=\'404 NOT FOUND\' THEN 1 ELSE 0 END))/(count\
(date(time))*1.0)*100),2) > 1;'

# Calls the fileOpen method to open the file NewsResults.txt for appending and
# creates an object.  Which is then stored in the variable file.

file = fileOpen()

# Calls the method connect to create a connection to the news database.
# Then this object is stored in the variable conn.

conn = connect()

# creates a cursor object to search the database.

curr = conn.cursor()

# Calls the searchData method and passes in a cursor, curr, an sql
# statement,  sql1, and two headers, header1 and header2. Then
# recieves the result of the query.

results = searchData(curr, sql1, header1, header2)

# Calls the method connect to create a connection to the news database.
# Then this object is stored in the variable conn.

file = fileOpen()

# Calls the searchData method and passes in a cursor, curr, an sql
# statement,  sql2, and two headers, header3 and header2. Then
# recieves the result of the query.

results = searchData(curr, sql2, header3, header2)

# Calls the method connect to create a connection to the news database.
# Then this object is stored in the variable conn.

file = fileOpen()

# Calls the searchData method and passes in a cursor, curr, an sql
# statement,  sql6, and two headers, header4 and header5. Then
# recieves the result of the query.

result = searchData(curr, sql3, header4, header5)

# Closes the file connection.

file.close()

# Closes the database connection.

conn.close()
