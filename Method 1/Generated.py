from datetime import datetime
from random import randrange
from time import time
import os
import csv
import WordList
import PhraseList
import ServicesList
import split_text
import uuid
import Random
from Messages import sendMail
import test   
# mail="yosrabenkridis02@gmail.com"
# def verifyU(Username,Service,Name):
#     data=open("users.txt","r")
#     file = data.read()
#    # print(file.split()[0])
#   # Username = input("Enter your username :")
#     split_text.split()
#     c= ServicesList.get_service(Service)
#     a= WordList.get_word() 
#     b= PhraseList.get_phrase()
#     pwd1 = b[1]+c[1]+a[1]+c[2]+"v1"            
#     modified_pwd = pwd1.replace("v1", 'v{}'.format(1) )
#     id=uuid.uuid4()
#     f = open("users.txt", "a")
#     f.write(str(id)+","+Name+","+Username+","+str((datetime.timestamp(datetime.now())))+","+modified_pwd+"\n")
#     f.close()
#     Random.Mise(mail)
#     return modified_pwd

# verifyU("yosrabenkridis02@gmail.com","Gmail",'yosra')
 
mail='yosrabenkridis12345@gmail.com'
 
def verifyU(Service): 
    # data=open("users.txt","r")
    # file = data.read()
    # file.split()
    # Username = input("Enter your username :")
    # Name = input("Enter your name :")
    split_text.split()
    c= ServicesList.get_service(Service)
    a= WordList.get_word() 
    b= PhraseList.get_phrase()
    pwd1 = b[1]+c[1]+a[1]+c[2]+"v0"            
    modified_pwd = pwd1.replace("v0", 'v{}'.format(0) )
    # id=uuid.uuid4()
    # f = open("users.txt", "a")
    # f.write(str(id)+","+Name+","+Username+","+str((datetime.timestamp(datetime.now())))+","+modified_pwd+"\n")
    # f.close()
    # Random.Mise(mail)
    return modified_pwd
    # print(modified_pwd)
# verifyU('Gmail')
import time
def update_web(existing_password: str) -> str:
    """Updates the given password.

    The updated password is generated by changing the letter before the @ symbol and the letter after the @ symbol to r1 and r2 respectively.

    Args:
        existing_password: The password to be updated.

    Returns:
        The updated password.    """
    # Call the verifyU function to get the existing password
    # existing_password = verifyU('Gmail')
    # Extract the version number from the existing password
    version_index = existing_password.rfind('v')
    version_number = int(existing_password[version_index + 1:])

    # Increment the version number
    updated_version_number = version_number + 1

    # Generate the updated password by changing the d and the c to r1 and r2 respectively
    r1 = chr(randrange(97, 122))
    r2 = chr(randrange(65, 90))
    updated_password = f"{existing_password[:7]}{r1}{existing_password[existing_password.index('@'):existing_password.index('@')+1]}{r2}{existing_password[existing_password.index('@')+2:version_index]}v{updated_version_number}"
    # updated_password = f"{existing_password[:7]}{r1}@{r2}{existing_password[9:version_index]}v{updated_version_number}"
        # Send an email with the updated password
    sendMail('yosrabenkridis02@gmail.com', "Password update !!", f"Your updated password is: {updated_password}")
    return updated_password

def Up():
    # Call the verifyU function to get the existing password
    existing_password = verifyU('Gmail')
    # updated_password = update_web(existing_password)
    # print(updated_password)
# Update the password repeatedly and print the result
    i = 0
    while True:
       updated_password = update_web(existing_password)
       print(updated_password)
       existing_password = updated_password
       i += 1

       # Sleep for 1 minute (60 seconds)
       time.sleep(10)
       os.system('cls||clear')
Up()

