def longest(centre , largest):
  checker = True
  counter = 1
#  import pdb;pdb.set_trace()
  while checker:
    if (centre+counter)<size and (centre-counter)>=0:
      if ( value[centre+counter] == value[centre-counter]):
        if (2*counter+1>largest):
          largest = 2*counter+1
 	  start = centre-counter
        counter +=1
      else:
        checker = False
    else:
      checker = False
  return largest


print 'Enter a string'
value = raw_input()
size = len(value)
largest = 1
start = 0
for i in range(size):
  largest = longest(i , largest)
print value[start:start+largest]
print largest
