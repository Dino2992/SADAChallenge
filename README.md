# SADA Challenge
SADA challenge Highest profit

For this coding challenge I used python and a .bat file to complete the different parts of this challenge. I have used python as it is the language that I am most comfortable with. 
In order for the run.bat file to work properly the user will have to attach their python.exe path from their computer into the run.bat file by editing the run.bat file.
Insert the python.exe path in the spot where the batch says to insert the path between the quotations. All other files needed to run the files are in the repository to be downloaded or cloned.
Below are the instructions for the challenge.


# Challenge
* First read the `Basic rules for challenges` (https://github.com/bobbae/gcp/blob/main/challenges/README.md).

* Summary: Read a CSV file containing corporate profits over the years and create JSON format data and look for highest profit values in the data.

## Part 1

* Download the data file at https://gist.github.com/bobbae/b4eec5b5cb0263e7e3e63a6806d045f2 as "raw" and read the file into a program memory.  

* The data file is in CSV format, the
comma separated values format.  

* Once the data is read into memory in your program, print out how many rows of the data is in the CSV data. This is your first printed answer.

* For each row, there are columns.  One of the columns is the "profit".  The data in this profit column
are not always valid.  Sometimes the data is non-numeric.  Remove all rows with 'profit' that is not numerical value. Then
print out how many rows of data are left, after removing all the rows with invalid non-numeric profit column data.  This is your second printed answer.


## Part 2

* You can now convert the content your read into memory in your program in Part 1 into JSON format and write it out to another file called `data2.json` which should only contain rows of data that have the valid numeric profit values. Each row in the Array should contain data columns like year, rank, company, revenue, and profit.

* Order the data based on the profit value.  Print the top 20 rows with the highest profit values. This is your third printed answer.

## Part 3

* Check and make sure your solution produces three answers as printed output. And a file called `data2.json` is produced.

* Think about how you may do this using SQL.  We may discuss other ways to solve this problem.  You don't need to write anything down, just think about different ways.
