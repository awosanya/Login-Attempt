                                        #SCRIPT WRITTER OLADIMEJI AWOSANYA

                                    ##### Login Authentication code Snippet #####
                                            ######  LOGIN ATTEMPT #########

"""
Instruction
===========
1. set the attempt parameter of the Login
2. Make a conditional statement to be fullfill by the attempt
3. Open or Connect to the DataBase file. I used a CSV File called memeberFile.csv...Inside the CSV
   file i have registered the first_name as awosanya and password as oladimeji in dictionary formart.
4. Request the User for user Name and Password
5. Use the information supply by the user to check if the data supply is in the database.
   If YES , Yeppee and if No reenter
    user name and password .
6. Ensure to import the storage file you want to use as Datababe
"""


import csv


attempt = 3
while attempt > 0:
    with open("memeberFile.csv",'r') as memberFile:
        userName = input("Enter User Name: ")
        userPassword = input("Enter Password: ")
        reader = csv.DictReader(memberFile)
        for memeberName in reader:
            if userName == memeberName['first_name'] and userPassword == memeberName['password']:
                print("successful Login")
                break
            elif userName != memeberName['first_name'] or userPassword != memeberName['password']:
                attempt -= 1
                print("Wrong password: ", attempt, "Attemp left")
else:
    print("Account Blocked")
    #Move the userName from memberFile.csv to memberAccountBlockFile.csv
    #For Move information on how to write that, PM me and follow me for the latest snippet

       



        #####   TO WRITE TO A CSV FILE #####
        ##### openning the DataBase File
                
   
##with open('memeberFile.csv', 'w') as csvfile:
##    fieldnames = ['first_name', 'password']
##    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
##
##    writer.writeheader()
##    writer.writerow({'first_name': 'Awosanya', 'password': 'oladimeji'})
