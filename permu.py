''' Program to calculate all the permutations of a string
    entered by the user '''

print 'Enter a string'
string = raw_input()
st = list(string)
pers=[]

def permu(st,val):
  va =  ''.join(st)
  if va not in pers:
    pers.append(va)
  for j in range(val,len(st)):
    st[val],st[j] = st[j],st[val]
    permu(st,val+1)
    st[val],st[j] = st[j],st[val]

for i in range(len(st)):
  permu(st,i)

print 'Output'
for per in pers:
  print per
print 'Count = '+str(len(pers))
