from random import random, randrange
from datetime import datetime
from xml.etree.ElementTree import tostring
from Messages import sendMail
import WordList
import PhraseList
import ServicesList
import split_text

import time
import os
os.system('cls||clear')

def main():

      enter=input('Enter the service : ')
      c= ServicesList.get_service(enter)

      while(c==[]):
            print('Invalide Service!')
            re_enter=input('Entrez une donnée again : ')
            c= ServicesList.get_service(re_enter)
      

      passwords=""    
      split_text.split()    
      for j in range(3):
                a= WordList.get_word() 
                b= PhraseList.get_phrase() 
                pwd= c[0]+str(j)+","+b[j]+c[1]+a[j]+c[2]+"v1"  
                modified_pwd = pwd.replace("v1", 'v{}'.format(1) )
                #print("Modified password:", modified_pwd)
                passwords = passwords + modified_pwd+"\n"
      f = open("pwd.txt", "w")
      f.write(passwords)
      f.close()
      print("Passwords file was updated !")
      time.sleep(3) 
    #   os.system('cls||clear')

def updateWeb():
    file = open("users.txt","r")
    passwords = file.read().split("\n")
    passwords=passwords[:len(passwords)-1]
    print(passwords)

    Npasswod=""
    for password in passwords:
        index= password.rfind(',')
        t=index+8
        y=index+10
        r1= chr(randrange(97,122))
        r2= chr(randrange(65,90))
        index2 = password.rfind(",",0, password.rfind(",")-1) 
        print(index2)
        timeset=datetime.timestamp(datetime.now())-float(password[index2+1:index]) #time of update
        print(timeset>=20) #20 seconde
        if (timeset>=20):
            newWord=password[:index2]+","+str(datetime.timestamp(datetime.now()))+','+password[index+1:t]+r1+password[t+1:y]+r2+password[y+1:password.rfind('v')]+"v"+str(int(password[password.rfind('v')+1:])+1) 
            to=password[password.find(",", password.find(",") + 1)+1:password.find(",", password.find(",",password.find(",") + 1) + 1)]
            body=password[password.rfind(',')+1:]+'\n'+"Your new password"
            sendMail(to,"Password Updated",body)
        else:
            newWord=password 
        Npasswod = Npasswod + newWord+"\n"
        print(timeset)
    f = open("users.txt", "w")
    f.write(Npasswod)
    f.close()
    print("Passwords file was updated !")
    time.sleep(3) 
    #os.system('cls||clear')
updateWeb()