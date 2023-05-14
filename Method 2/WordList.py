##############################################################################################################
###################################### get_word() function ###################################################
# List of words taken from file Words.txt                                                                    #
# Creation of an empty table                                                                                 #
# Word hash with sha1                                                                                        #
# Each word hash is selected according to the last letter of hashed word taken according original word length#
# Remplir the table with the word hash                                                                       #
##############################################################################################################

import random 
import hashlib

file = open("Words.txt","r")
#======> the path where the file exist
words = file.read().split("\n")
#======> read the exist file
#======> The split() method divides a String into an ordered list of substrings, puts these substrings into an array, and returns the array.
#======> \n back to line
#print(len(words))
def get_word():
  n=0
  tab=[]
   #======> empty table
  while n<270 :
     valid_word = False
     #======> the enter word is not valide yet
     while(not valid_word):
         index = random.randint(0,len(words))
         #======> method returns an integer number selected element from the specified range randomly
         word = words[index-1]
         #======> method returns the index of the specified element in the list.
         if(word[0].islower() and len(word)>4):
           #======> condition the word must be lower and it lenth bigger then 2
             valid_word = True
             #======> valide the word 
             #print(word)
             sha1Hash = hashlib.sha1(word.encode())
             sha1Hashed = sha1Hash.hexdigest()
             hashed_word=sha1Hashed[-len(word):]
             #======> word hash and display of hashed word and its length 
             #======> is selected according to the last letter of hashed word taken according original word length
             tab.append(hashed_word)
             
             #======> add the element at end of the list ( random )

     n=n+1
  return tab
#======> return a table of words




