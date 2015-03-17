'''Function to check for a number bomb( three consecutive pairs of integers) in an integer array '''

def  contains_bomb( arr):
    counter = 0    # Net checker to see if 3 pairs are reached 
    count = 1      # Counting instances of each integer
    for i in range (1,len(arr)):
        if (arr[i] == arr[i-1]):
            count = count+1
        else :
            # Condition to check if the previous integer had more than 2 instances
            if count>=2:
                  counter = counter+1
                  if counter == 3:
                    return True
                
            else:
                counter = 0
            count = 1
            # Condition to check if the new integer and previous are consecutive
            if arr[i]!=arr[i-1]+1:
                counter = 0
        
    if count>=2:
      counter =counter+1
    if counter == 3:
            return True    
    return False    
