#prompt the user

#import the sqlite3 library
import sqlite3

#create the connection object
with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    prompt = '''
    Select the operation that you want to perform [1-5]
    1. Average
    2. Max
    3. Min
    4. Sum
    5. Exit
    '''

    #loop until user enters a valid operation nymber [1-5]
    while True:
        #get user input
        x = input(prompt)

        #if user enters any choice from 1-4
        if x in set(["1","2","3","4"]):
            # parse the corresponding operation text
            operation = {1:"avg",2:"max",3:"min",4:"sum"}[int(x)]

            #retrieve data
            c.execute("Select {}(num) from numbers".format(operation))

            #fetchone() retrieves one record from the query
            get = c.fetchone()

            #output result to screen
            print(operation + ": %f" % get[0])
        #if user enters 5
        elif x == "5":
            print("Exit")

            #exit loop
            break


