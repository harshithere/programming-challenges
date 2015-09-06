''' Following program counts the number of n-digit numbers that have sum equal to
    a given number entered by the user '''

print " Enter n and sum"
val = raw_input().split(' ')
n = int(val[0])                # Input containing number of digits in the number
sum1 = int(val[1])             # Input containing required sum of digits
first_iter_check = False       # Boolean variable to check if its first digit
print n,sum1

def get_ans(num, sum2):        # Function get count of numbers with specified sum
  if num==0:
    return sum2 == 0           # Returns 1 if match digit sum is equal to required sum
  
  count = 0
  global first_iter_check
  if not first_iter_check:     # First digit can't start with 0. This condition is used to check that
    first_iter_check = True
    start = 1
  else:
    start = 0
  for i in range(start,9):
    if sum2>=i:
      count += get_ans(num-1,sum2-i)    # Recursive function
  return count

count = get_ans(n, sum1)
print 'Count :' +str(count)
