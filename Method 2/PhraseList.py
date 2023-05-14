#############################################################################################################
######################################### get_phrase() Function #############################################                                                                                                      
# List of phrases taken from file Phrases.txt                                                               #                                                                                                        
# Creation of an empty table                                                                                #
# take the 2 first letters from each word in the phrase and concatunate them                                #
# uppercase randomly the cancatunate word                                                                   #                                                                                                          
##############################################################################################################

import random 

file = open("Phrases.txt","r")
#======> the path where the file exist
phrases = file.read().split("\n")
#======> read the exist file
#======> The split() method divides a String into an ordered list of substrings, puts these substrings into an array, and returns the array.
#======> \n back to line
#print(len(phrases))

def get_phrase():
  n=0
  t=[]
  #======> table vide
  while n<270 :
     valid_phrase = False
     #======> the enter phrase is not valide yet
     while(not valid_phrase):
         index = random.randint(0,len(phrases))
         #======> method returns an integer number selected element from the specified range randomly
         phrase = phrases[index-1]
         #======> takes a list of sentences and a list of words
         if(phrase[0].islower() and len(phrase)>2):
             #======> condition the word must be lower and it lenth bigger then 2
             valid_phrase = True
              #======> valide the phrase
             tab=phrase.split()
             #======> table view each table contient the words of the phrases
             #======> split(empty)--> delete the space
             Uword=""
             #======> empty word 
             for w in tab:
               r=random.randint(0,1)
               #======> method returns an integer number selected element from the specified range randomlys
               if r==0:
                Uword=Uword+w[0:1].upper()+w[1:2]
                #======> uppercase in the first letter
               else:
                Uword=Uword+w[0:1]+w[1:2].upper()
                #======> uppercase in the second letter
             t.append(Uword)
             #======> add the element at end of the list (random)
     n=n+1
  return t
#======> return a table of phrase


