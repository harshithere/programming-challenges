
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

arr = input()
print arr
result = quick_sort(arr)
print result
