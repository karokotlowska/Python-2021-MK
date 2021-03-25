import random
import math
import copy
import string

### 1
k=int(input('k=? '))
lista=[random.randint(0,5*k) for i in range(k)]
#print(lista)

liczba=0
slownik={}
lista1=copy.deepcopy(lista)
for i in range(100):
  random.shuffle(lista1)
  for j in range(k):
    if lista1[j]==lista[j]:
      liczba+=1
  slownik[i+1]=liczba
  liczba=0

#print(slownik)

### 2
slowo=string.ascii_lowercase
a=''.join(random.choice(slowo) for i in range(k))
b=list(a)
#print(b)
for i in range(1,k*2,2):
  b.insert(i,'.')
#print(b)

### 3
l=[random.randint(0,20)for i in range(100)]
s1={}
s2={}
for i, v in enumerate(l):
  if not s1.setdefault(v,[i])==[i]:
    s1[v].append(i)
#print(s1)

for i in l:
  s2.setdefault(i,[])
  if len(s2[i])>=1:
    x=s2[i][-1]
  else:
    x=-1
  s2[i].append((l[x+1:].index(i))+x+1)
#print(s2)


### 4
n=random.randint(3,7)
print(n)
lista2=[random.randint(10**(n-1),10**n)for i in range(10)]
print(lista2)

sp={}
print(n//2)
for i in range(10):
  p=True
  for j in range(n//2):
    if lista2[i]//(10**(n-j-1))==(lista2[i]-lista2[i]//(10**(n-j+1))):
      pass
    else:
      p=False
  if p:
    sp[i]=i
print(sp)

### 5
slownik1={}
slownik2={}
for i in range(10):
  slownik1[i]=random.randint(1,100)
  slownik2[i]=random.randint(1,100)

#print(slownik1)
#print(slownik2)

for i in range(10):
  z1=dict((v,k) for k,v in slownik1.items())
  z2=dict((v,k) for k,v in slownik2.items())
#print(z1)
#print(z2)

slownik3={}
for i in z1:
  if i in z2:
    slownik3[i]=(z1[i],z2[i])
#print(slownik3)