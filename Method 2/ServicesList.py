file = open("Services.txt","r")
services = file.read().split("\n")
#print(len(services))
def get_service(input):
  tab=[]
  n=0
  while n< 10 :
     valid_service = False
     while(not valid_service):      
         service = services[n]
         valid_service = True
         t= service.split()
         if t[0] == input:
          for service in t:
           tab.append(service.encode("latin-1").decode("utf-8"))

     n=n+1
  return tab
#get_service("Gmail")





