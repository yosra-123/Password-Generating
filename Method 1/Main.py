##############################################################################################################
############################################### Main #########################################################
# Importation of the file of the function                                                                    #                                                                                                           
# Function call with declaration of variable                                                                 #
# Concatunation of the functions                                                                             #
##############################################################################################################

#======> importation of the file of the function
from xml.etree.ElementTree import tostring
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
      
      
      for i in range(5) :
            passwords=""    
            split_text.split()    
            for j in range(3):
                  a= WordList.get_word() 
                  b= PhraseList.get_phrase() 
                  pwd= c[0]+str(j)+","+b[i]+c[1]+a[i]+c[2]+"v1"  
                  modified_pwd = pwd.replace("v1", 'v{}'.format(i+1) )
                  #print("Modified password:", modified_pwd)
                  passwords = passwords + modified_pwd+"\n"
            f = open("pwd.txt", "w")
            f.write(passwords)
            f.close()
            print("Passwords file was updated !")
            time.sleep(3) 
            os.system('cls||clear')
           
            
