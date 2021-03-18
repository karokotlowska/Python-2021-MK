import copy 

k=[]
print(type(k))
'''
k=[2,]
print(type(k))

k=[1,2.3,'3',(3,4),[2,3,4]]
print(k[0],k[-1])'''
'''
k=[8,0,17,1,10,13,19,13,10,3,]
print(k[:])
print(k[2:-3])
print(k[2:-3:3]) #trzecia wartosć - bierze co którąs liczbe

print(k[::-1]) #odwrócenie kolejności w liście

k=[1,2.3,'3',(4,7),[2,3,4],]
c=k #płytka kopia listy
c[1]=[7,8,9]
print(c,k)
print(id(c),id(k)) #wypisanie id - wypisuje ten sam "adres"

c=k[:] ##kopiowanie gebokie, przydatne przy tworzeniu listy zawierającej elementy niemodyfikowalne
c[1]='8,7,6'
print(c,k)
print(id(c),id(k))

c[-1][1]='8,7,6'
print(c,k)

c=k.copy()
c[1]='4,5,6'
print(id(c),id(k))
c[-1][1]='8,7,6'
print(c,k)

mozemy tez importowac bilioteke copy i skorzystac z modulu deepcopy

c=copy.deepcopy(k)
c[1]='4,4,4'
print(c,k)'''

k=[8,0,17,1,10,13,19,13,10,3,]
print(k.count(13))
print(k.count(-13))
print(k.index(13)) #zwraca indeks występowania elemetu 13
#print(k.index(-13)) - daje bład
print(13 in k)
print (13 not in k)

if 13 in k:
  pass

if 13 not in k:
  pass

#jkabysmy chcieli wyszukac drugą trzynastjke w liscie
i=k.index(13)
k.index(13,i+1)


print(k)
k.insert(4,-13) #dodaje 13 pod indeksem 4 a reszta jest przesuwana o 1 w prawo
print(k)

k.insert(-23,4) #jesli indeks przekracza zakres to wstawia na poczatku
k.insert(23,4) #jesli indeks przekracza zakres to wstawia na koncu
print(k)

k[1:4]=[10,18,19,110,] #wstawia zamiast tych elementow przy k
print(k)
k[1:4]=[[7,8,],]
print(k)

#usuwanie
k.remove(1)
k.remove(110) #usuwa liczbe 110
print(k)

del k[3] #usuwa element o indeksie 3, jesli podamy niepoprawny parametr to mamy wyjatek
print(k)

del k[-3:] #usuwa 3 elementy
print(k)

print(k.pop())
print(k)

print(k.pop(-3))#usuwa element o ineksie -3 i go zwraca
print(k)

k.clear() #usuwa wzytsko
print(k)


k=[1]*10 #tworzy liste z 10 jedynkami w srodku
k[3]+=1 #dodaje 1 do elementu o 3 indeksuie
print(k)


k=[[]]*10 #lista zawierajaca 10 pustych list
k[3].append(3) #dodaje 3 do wszystkich elementów, ale to dlatego ze jest na obiekcie bo obiekty sa kopiowane przez referencje
print(k)


k=[[] for _ in range(10)] #lista składana
k[3].append(1) #dodawana jest 1 dla 3 indeksu, append modyfikuje tylko 1 konkretna liste
print(k)

k[3].append([1,2,3]) #dodaje obiektu jako całości
print(k)

k=[]
for _i in range(10):
  k.append(_i)
print(k)

k=list(range(10))
print(k)
k=list(range(4,10))
print(k)
k=list(range(3,10,2))#ostatni parametr to krok
print(k)
k=list(range(10,0,-1))#dodaje elementy od konca
print(k)

k=[8,0,17,1,10,13,19,13,10,-3,]
for i in k:
  i*=2
  print(i,end=', ')
print('\n',k)

for i in range(len(k)):
  k[i]*=2

for i, v in enumerate(k):
  k[i]=1 if v>0 else -1
print('\n',k)
#krotka zwracana przez enumeratme, V- wartosc


for i in k:
  if i%2:
    break
  else:
    print("kiedy")
#kiedy wyniik bedzie równy 0


np=[i for i in k if i%2] #tu w liscie beda liczby parzyste
np=[1 if i>0 else -1 for i in k]



k=[(k[i],k[-i-1])for i in range(len(k)//2)]
print(k)
#do listy wsipuje elemetnt pierwszy i ostatni, drugi i przedostatni itp
#dwa ukośniki mówią odzieleniu całkowitym
for i,j in k:
  print(i,j)

k=[(89,34),(92,36),(96,0),(48,30),(38,10)]
c=k[:] #tworze kopie
c.sort() #wywoluje metode sort
#c=c.sort() - wypisuje sie wartosc none, bo tak nie wywolujemy, bo sort dziala w miejscu
print(c)
#lista postortowala sie co do wielkosci pierwszego elemntu krotek

c=k[:]
c.sort(key=lambda x:x[1])
print(c)


c=k[:]
c.sort(reverse=True)
print(c)

c=k[:]
for i,j in sorted(k):
  print(i,j)
print(c)

c=k[:] #posortowanie w odrotnej kolejnosc
c.sort(reverse=True)
print(c)


c=k[:] #odwraca elementy listy
c.reverse()
print(c)

c=k[::-1] #odwraca elementy listy
print(c)


#############################
k=[8,0,17,1,10,13,19,13,10,3,]
print(k)
for i in range (k.count(10)):
  k.remove(10)
print(k)


##############################
k=[8,0,17,1,10,13,19,13,10,3,]
while k.count(10):
  k.remove(10)
print(k)

#############################
k=[8,0,17,1,10,13,19,13,10,3,]
print(k)
for i in range(0,len(k),2):
  print(k[i])


#############################
print(k)
l=[(i,k[i]) for i in range(10)]
print(l)  


#############################
k.sort(reverse=True)
print(l)
