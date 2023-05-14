import WordList
import PhraseList
import ServicesList
import split_text
import Main
import time
import os
import csv

os.system('cls||clear')

def verifyU():
   data=open("pwd.txt","r")
   file = data.read()
   Username = input("Enter your username :")
 
   if Username in file:
        print("Username exists")
        verifyU()
   else:
       #data = open("users.txt","a")
       #data.write(Username+","+giveP()+"\n")
       print("success!")

   Service=input('Enter the service : ')
   c= ServicesList.get_service(Service)

   while(c==[]):
         print('Invalide Service!')
         re_enter=input('Enter again : ')
         c= ServicesList.get_service(re_enter) 
   for i in range(1) :
    
      split_text.split()    
     
      for j in range(1):       
           a= WordList.get_word() 
           b= PhraseList.get_phrase()
           pwd1 = b[i]+c[1]+a[i]+c[2]+"v1"            
           modified_pwd = pwd1.replace("v1", 'v{}'.format(i+1) )
           print("Your password is :", modified_pwd)
      f = open("pwd.txt", "a")
      f.write(Username+","+modified_pwd+"\n")
      f.close()
      #print("Passwords file was updated !")
      #time.sleep(3) 
      #os.system('cls||clear')      
verifyU()



