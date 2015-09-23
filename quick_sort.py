''' Following program arranges an array of digits using quick sort. It uses
    a recursive stratergy where we assign first element as the central element 
    and recur for subarrays on left and right.'''

def quick_sort(arr):
  left = []
  right = []
  same = []
  if len(arr)<=1:
    return arr
  center = arr[0]
  for i in arr:
    if i<center:
      left.append(i)
    elif i>center:
      right.append(i)
    else:
      same.append(i)
  
  less = quick_sort(left)
  more = quick_sort(right)
  return less + same +more

print 'Enter the digits which are to be sorted as an array'
arr = input()
print arr
result = quick_sort(arr)
print 'The array after sorting is -'
print result
