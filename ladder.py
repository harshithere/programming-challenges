'''Program to find length of a ladder given its heigth and angle'''

import math

#Get inputs
values = raw_input().split(' ')

heigth = int(values[0])
angle = int(values[1])

angle = math.radians(angle)  #Convert angle into radians
print int(round((height/math.sin(angle))))
