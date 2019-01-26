fullstack-nanodegree-vm
=============

Common code for the Relational Databases and Full Stack Fundamentals courses

## The Project Log Analysis Article Database Search
====================================================

This program will search the news database using three different queries.
The first, will search, and calculate, the top three articles viewed.  The second,
will search, and calculate, the top four authors of all time. And the third, will 
calculate the percentage of 404 errors recieved each day.  All of this information 
will then be written to the  file named NewsResults.txt

# Quick Start
--------------

* Install Vagrant <a href="https://www.vagrantup.com/">Vagrant Download</a>
  Download and run the proper file for your operating system.

* Install Python3 <a href="https://www.python.org/">Python Download</a>
  Go to the downloads section and run the installation file python-3.7.2.exe.

* Install Virtual Box<href="https://www.virtualbox.org/wiki/Download_Old_Builds_5_1"></a>
  And download and install the proper version for your operating system.
  
* Start Git Bash

* Change into the directory that want to program to reside.
  
* Clone a copy of the git repository using the following command: git clone https://github.com/FreemanWillaim/ProjectLogAnalysis.git

* Move into the vagrant directory.

* Enter at the command prompt: vagrant up.

* Change yor working directory to vagrant by typing cd .. twice and then changing into the vagrant directory.

* To download a copy of the newsdata database click on the following link:
  https://classroom.udacity.com/nanodegrees/nd004/parts/51200cee-6bb3-4b55-b469-7d4dd9ad7765/modules/c57b57d4-29a8-4c5f-9bb8-5d53df3e48f4/lessons/bc938915-0f7e-4550-a48f-82241ab649e3/concepts/a9cf98c8-0325-4c68-b972-58d5957f1a91

* Click on download data here.

* Place the newsdata zip file in your vagrant directory.

* unzip the newsdata file.

* Move the newsdata file from the newly created folder called newsdata to the vagrant directory.

* While in the vagrant directory type the following command to install the database:  psql -d news -f newsdata.sql

* Now that the news database has been installed, change the working directory to news.

* At the command prompt type: python news.py.


# Explanation of my Code
------------------------

This code will connect to the news database and run several queries against it and output the results to a text file 
named NewsResults.txt. A number of headers are then created to hold the headers for the table that will be written to 
the text file. Three queries are then created to search the records of the database.  The fileOpen and connect meathods 
are then called.  A cursor is created next to preform searches of the databases records.  The searchDataBase and fileOpen 
method are then called to execute the three queries, and to write the results to the text file.  The file and database 
connection are then closed.

In the first part of the program five strings are created.  These strings will represent the header for each column for the 
table that will be created in the text file.  The first string is called header1 and will contain the string Title. 
The second string is called header2 and will contain the string Views. The third string is called header3 and will contain the string Author.
The forth string is called header4 and will contain the string Date. And finally, a fifth string is created called header five
and it contains the sting Percentage of Errors.

The three SQL queries that are created to run against the database are called sql1,sql2, and sql3.  The first sql query 
calls the searchData method and passes in a cursor, curr, an sql statement, sql1, and two headers, header1 and header2. Then
recieves the result of the query.  The second sql query calls the searchData method and passes in a cursor, curr, an sql
statement,  sql2, and two headers, header3 and header2. It then recieves the result of the query.  The third and final sql query
calls the searchData method and passes in a cursor, curr, an sql statement,  sql6, and two headers, header4 and header5. Then
recieves the result of the query.

The program the calls then fileOpen method to open the file NewsResults.txt for appending. Nothing is passed into this method but
connection to the file NewsResults.txt is created and a file object is passed back and stored in the variable file.

A connection to the database is created by calling connect method. This method connects to the news database and returns this
connection in the variable conn. 

A cursor object is create and stored in the variable curr.  This opbject will be used to search through the news database.

Next, the searchData method is called and the curr object, sql1, header1 , and header2 strings are passed into this method.
This method will execute the query stored in the variable sql1, retrieve the result of that query, and then call the method
display which will write those results to the ouput file.

The display method will accept the result of the query and two header1 and header2. This method will then loop through those results 
and write header1, the results of the query, and header2 to the output file. Then close the file.

Then, the searchData method is called again, and the curr object, sql2, header2 , and header3 strings are passed into this method.
This method will execute the query stored in the variable sql2, retrieve the result of that query, and then call the method
display which will write those results to the ouput file.

The display method will accept the result of the query and two header2 and header3. This method will then loop through those results 
and write header2, the results of the query, and header3 to the output file. Then close the file.

the final call to the searchData method is made and the curr object, sql3, header4 , and header5 strings are passed into this method.
This method will execute the query stored in the variable sql3, retrieve the result of that query, and then call the method
display which will write those results to the ouput file.

The display method will accept the result of the query and two header4 and header5. This method will then loop through those results 
and write header4, the results of the query, and header5 to the output file. Then close the file.
   
Finally, the connection to the file and database are closed.