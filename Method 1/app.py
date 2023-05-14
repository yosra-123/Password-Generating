from datetime import datetime
from time import time
from flask import Flask, request_finished, session, render_template, request, redirect, g, url_for
#from flask_session import Session
import os
import csv
import WordList
import PhraseList
import ServicesList
import split_text
import uuid

def verifyU(Username,Service,Name):
   data=open("users.txt","r")
   file = data.read()
  # Username = input("Enter your username :")
 
   if Username in file:
        print("Username exists")  
        # verifyU()
        return False
  # else:
       #data = open("users.txt","a")
       #data.write(Username+","+giveP()+"\n")
       #print("success!")

   #Service=input('Enter the service : ')
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
           id=uuid.uuid4()
           #print("Your password is :", modified_pwd)
        
      f = open("users.txt", "a")
      f.write(str(id)+","+Name+","+Username+","+str((datetime.timestamp(datetime.now())))+","+modified_pwd+"\n")
      f.close()
      return modified_pwd
      #print("Passwords file was updated !")
      #time.sleep(3) 
      #os.system('cls||clear')      
#verifyU()


def access(Username,Password):

    if not len(Username or Password)< 1:

        with open("users.txt","r") as data:
            file_reader = csv.reader(data)
            for row in file_reader:
                
                if row[2] == Username:
                   # print("username found", Username)
                    user_found = [row[2],row[4]]
                    if user_found[1] == Password:
                        return True
                    #else:
                        #print("password not match")                           
                    
                    break  

#access()   
app = Flask(__name__)

app.secret_key = os.urandom(24)

@app.route('/register', methods=['GET','POST'])
def register():
    
    if request.method=='POST':
        ok=verifyU(request.form['username'],request.form['Service'],request.form['name'])
        if ok:

            return render_template('createSuccess.html',username=request.form['username'],service=request.form['Service'],pwd=ok)
        
        else:
                return render_template('ErrorRegister.html')
                
    return render_template('register.html')
   

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        session.pop('user',None)

 
        if access(request.form['username'],request.form['password']):

            session['user'] = request.form['username']
            
            return redirect(url_for('protected'))
        
        else:
                return render_template('error.html')
    return render_template('index.html')



@app.route('/protected')
def protected():
    if g.user:
        return render_template('protected.html', user=session['user'])
    return redirect(url_for('index'))



@app.before_request
def before_request():
    g.user = None

    if 'user' in session:
        g.user = session['user']



@app.route('/dropsession')
def dropsession():
    session.pop('user',None)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)





