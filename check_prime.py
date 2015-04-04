''' Program to check whether a given number is prime or not '''

import math

def isprime(num):
  if num<2:
    return False
  elif num == 2:
    return True
  else:
    for i in range(3, int(math.sqrt(num))+1 , 2):
      if num%i==0:
        return False
  return True

print "Enter a number to check"
num = int(raw_input())
result = isprime(num)
if result:
  print 'Number is prime'
else:
  print 'Number is not prime'
