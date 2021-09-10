# SADA Challenge
SADA Challenge Highest-Profit

For this coding challenge I used Python and a .bat file to complete the different parts of this challenge. I have used Python as it is the language that I am most comfortable with. 
The reviewer will run one script run.bat. Prior to executing the script the reviewer will have to attach their python.exe path into the run.bat file. This can be done by right-clicking on the run.bat file and selecting edit.
After clicking edit and a new window opens, the reviewer will past their python.exe path into the spot area labeled "Put path of python.exe here in between the quotes". Do not include quotes around path or the file path will not read properly.
After pasting the path the reviewer will click save, which is under file tab so that way the run.bat will run properly.
Once that is complete the reviewer will just have to click the run.bat file and the script will be executed. The input needed for the Highest-profit challenge is the data file in CSV format, available below in the url. This data is also available when the repository is downloaded.
The outputs for the Highest-profit challenge are as follows. The first printed output is how many rows of data are in the CSV data. The second printed output will be how many rows of data are left after removing all the rows with invalid non-numeric profit column data.
Another output for this challenge is a json file named data2 which includes only rows of data that have valid numeric profit values. Each row in the array contain data columns such as year, rank, company, revenue, and profit. The last printed output contains the top 20 rows with the highest profit values.
As a suggestion, since python.exe is located in different paths based on how the computer or network is configurated a common path for the python executable would be favorable and allow the script to run without editing. The only other suggestion I have is that the printed outputs should be formatted to be more descriptive.

Below are the instructions for the Highest profit challenge.


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
