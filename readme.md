# Creating a Website that Displays our Dataset
### Creating a Database and Adding our Data to the Database 
To upload a data set to our website we had to keep the data set inside a dataase and then we used the sqlite as a database 
we created a connection  to the database called 'database.db' and created a cursor
we then read the data set file with pandas and added it to a table in the sql data base called goal_table
we did this so the data would be stpred in a table in the data basde that we created, and after adding all the data to the table we extracted all the data using the .fetchall() method 
we finally committed our changes to save all the work we had done and then we closed the connection 
we did all that with a functiion called create_database, we defined this functioin and the function does all the pfrocess for us and the function is saved in the python file called db_fillin.py

## Creating a Website Using Flask and Uploading the Database Data on the website 
This was all saved in the appproject .py python file 
we wrote code to import all the necessary packages needed to complete the task 
we then run code to create a website using flask and we created a homepage and an about page and a data page 
and we put the links to the about page and the dat apage on the home page for ease of access to those pages, we also did some basic html formatting to make the data appear as a table
and we connected to the cursor and added the created data base table to the data page of the website and saved all that in the python file 
and then we set the debug parameter to be true so that any changes made to the website can be seen without closing the connectionso we can just refresh the web page 

And to run the code we open the anaconda terminal and type in the following commands (pyhon appproject.py) and then it woulmd give you a link that givs you access to the website


The Templates folder would also be added , it is the basic html guide that we used to format our table 

