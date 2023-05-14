from cmath import e
from os import remove
from random import random
from bs4 import BeautifulSoup
import requests
import re
#regular expression
import random



def split():
  try:

      source = requests.get("https://techcrunch.com/")
      source.raise_for_status()
          
      soup = BeautifulSoup(source.text,'html.parser') 
      movies = soup.findAll('div',class_="content")[1].find_all('div',class_="post-block")
      # print(movies)
      para=''
      for movie in movies:
        name = movie.find('div',class_="post-block__content").text.strip().lower()
        s=re.sub('[^a-z]+', ' ', name)
        s=re.sub(r'\b\w{1,3}\b', '', s)
        s=s.strip()
        para=para+s
      tab=para.split()
      # print(tab)

  except Exception as e:
    print(e)

  def get_list_of_world(t):
    ball=""
    for i in range(100):
      num=random.randint(0,len(t)-1)
      ball=ball+t[num]+"\n"
    return ball.strip()

  words = get_list_of_world(tab)
  f = open("Words.txt", "w")
  f.write(words)
  f.close()
  # print("words list update")


  def get_list_of_phrases(tab):
    basket=""
    for j in range(100):
      n1=random.randint(0,len(tab)-1)
      n2=random.randint(0,len(tab)-1)
      n3=random.randint(0,len(tab)-1)
      n4=random.randint(0,len(tab)-1)
      #print(tab[n1]+' '+tab[n2]+' '+tab[n3]+' '+tab[n4])
      basket=basket+tab[n1]+' '+tab[n2]+' '+tab[n3]+' '+tab[n4]+"\n" 
    return basket.strip()


  phrases=get_list_of_phrases(tab)
  f = open("Phrases.txt", "w")
  f.write(phrases)
  f.close()
 # print("phrases file updating")
