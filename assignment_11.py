#Question 1

import time
import datetime
import threading

def threadd():
   time.sleep(5)
   print("Inside the function after 5 seconds")
      
threadd()


#Question 2

import time
import datetime
import threading

def numbers():
   i=1
   for x in range(10):
      print(i)
      i+=1
      time.sleep(2)
      
numbers()



#Question 3

import time
import datetime
import threading

l1 = [1,2,3,4,5]
def printl(l1):
   i = 2
   for x in l1:
      time.sleep(i)
      print("number: ",x)
      i+=2

printl(l1)



#Question 4

import time
import datetime
import threading

class Factt(threading.Thread):
   def __init__(self,n):
      threading.Thread.__init__(self)
      self.n = n
      
   def run(self):
      fact = 1
      while(self.n>0):
         fact = fact*self.n
         time.sleep(1)
         self.n = self.n-1
      print("Factorial: ",fact)
      

thread1 = Factt(5)
thread1.start()

