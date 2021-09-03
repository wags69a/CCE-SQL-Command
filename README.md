# CCE-SQL-Command
Using python, go into ICM database and pull information.
This is only 1 command from the SQL database, there are many more. This script gives you the foundation to build more.

#Installation 
I used python on my PC which had access to the customer's environment. You will have to adjust to your customer. This also works with any lab that you have access too.

#Usage 
This code can be to be used in a customer environment or a lab. It will change from each user. You will need connection access, user name, password and IP address. This script is the base for making more queries from the SQL database in UCCE and PCCE. This script will pull the information from the table you run the query on. This example is the Agent Targeting Rules table. It then prints the column names so you can compare the information. This script used an example with just one row of output, but if you run this on the Agent table, you can get 100s of responses depending on your build.

#DevNet Sandbox 
UCCE or PCCE sandboxes with SQL databases can use this script.

#Known issues 
In a later version, I hope to add a row count. The Agent table can be large and we will need to know if we have to put in a wait of a few seconds to let every row time to be printed out.

#Getting help 
Contact the owner if he is not too busy.

#Credits and references 
Stack Overflow gave me some of the ideas to try.
UCCE Staging and Installation guides.
UCCE develpoment guide.

#Best Practice 
Log into the SQL database on the UCCE logger or AW and execute the command to verify it works. 

#Step by Step

    Download python script based on the operating system you use to run the script.
    PIP install the requirements.
    Edit the file with your IP Address, password and databae name.
    Edit the python script to open and then print out a text file on your PC. The path in this script will be different than your own.
    Run the script.
    The script will pop open a notepad text file when completed.

#Example Output 
(5000, 5000, 1, None, None, 'ATRRULE1', None, 8, datetime.datetime(2017, 3, 22, 7, 51, 3, 977000))

AgentTargetingRuleID
PeripheralID
RuleType
TranslationRouteID
Expression
EnterpriseName
Description
ChangeStamp
DateTimeStamp
